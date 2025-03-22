from flask import Flask, request, jsonify
import subprocess
import json
import time
import logging
import concurrent.futures

app = Flask(__name__)
docker_compose_file = "/app/Scaling.yaml"

logging.basicConfig(level=logging.INFO)
executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

# Function to get the current count of any container type
def get_container_count(service_name):
    cmd = f"docker ps --filter 'name={service_name}-' --format '{{{{.Names}}}}' | wc -l"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        count = int(result.stdout.strip() or 0)  # Default to 0 if empty
        logging.info(f"Current container count for {service_name}: {count}")
        return count
    else:
        logging.error(f"Failed to get count for {service_name}: {result.stderr.strip()}")
        return 0  # Return 0 on error to avoid crashes

# Function to scale a specific service separately
def scale_service(target_service, new_target_count):
    """Scales only the target service without affecting others."""
    
    logging.info(f"Scaling {target_service}: New count -> {new_target_count}")

    scale_command = f"docker-compose -f {docker_compose_file} up -d --scale {target_service}={new_target_count} {target_service}"

    
    process = subprocess.Popen(scale_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, executable="/bin/bash")
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        logging.info(f"Successfully scaled {target_service}: New count -> {new_target_count}")
    else:
        logging.error(f"Failed to scale {target_service}: {stderr.decode()}")

    time.sleep(10)  # Adjust the duration as needed

    cmd = f"docker ps --filter 'name={target_service}-' --format '{{{{.Names}}}}' | wc -l"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        running_count = int(result.stdout.strip() or 0)  # Default to 0 if empty
        logging.info(f"Current running count for {target_service}: {running_count}")

        if running_count < new_target_count:
            logging.warning(f"Some containers are not running for {target_service}. Attempting to start them.")
            # Start the containers that are not running
            for i in range(running_count, new_target_count):
                container_name = f"slicing-upf_smf_ues-{target_service}-{i + 1}"  # Adjust this for the naming convention
                start_command = f"docker start {container_name}"
                start_process = subprocess.run(start_command, shell=True)
                if start_process.returncode == 0:
                    logging.info(f"Successfully started container {container_name}")
                else:
                    logging.error(f"Failed to start container {container_name}")
    else:
        logging.error(f"Failed to check running containers for {target_service}: {result.stderr.strip()}")


# Handle alert and trigger scaling
def handle_alert(data):
    if 'alerts' in data:
        for alert in data['alerts']:
            alert_name = alert['labels'].get('alertname')

            if alert_name == 'ScaleUPF':
                new_upf_count = get_container_count("upf") + 1
                executor.submit(scale_service, "upf", new_upf_count)
                new_smf_count = get_container_count("smf") + 1
                executor.submit(scale_service, "smf", new_smf_count)

            elif alert_name == 'ScaleSMF':
                new_smf_count = get_container_count("smf") + 1
                executor.submit(scale_service, "smf", new_smf_count)

@app.route('/alert', methods=['POST'])
def alert():
    """Webhook endpoint to receive alert and trigger scaling."""
    data = request.json
    logging.info(f"Received Alert: {json.dumps(data, indent=4)}")
    executor.submit(handle_alert, data)  # Run in parallel
    return jsonify({"status": "Scaling triggered"}), 200

@app.route('/')
def home():
    return "Scaling Webhook for UPF and SMF is Running!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
