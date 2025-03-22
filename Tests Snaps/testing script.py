import subprocess
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def get_docker_containers():
    """Get a list of running Docker containers."""
    try:
        result = subprocess.check_output(
            ["/usr/local/bin/docker", "ps", "--format", "{{.Names}}"], stderr=subprocess.STDOUT
        )
        containers = result.decode().splitlines()
        logging.info("Running containers:")
        for container in containers:
            logging.info(f"- {container}")
        return containers
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing Docker command: {e.output.decode()}")
        return []

def get_container_ip(container_name):
    """Get the IP address of a Docker container."""
    try:
        result = subprocess.check_output(
            ["/usr/local/bin/docker", "inspect", "-f",
             "{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}", container_name],
            stderr=subprocess.STDOUT
        )
        return result.decode().strip()
    except subprocess.CalledProcessError:
        logging.warning(f"Could not retrieve IP for {container_name}")
        return None

def check_iperf3_installed(container_name):
    """Check if iperf3 is installed in the container."""
    try:
        subprocess.check_output(
            ["/usr/local/bin/docker", "exec", container_name, "which", "iperf3"],
            stderr=subprocess.STDOUT
        )
        return True
    except subprocess.CalledProcessError:
        logging.warning(f"iperf3 not found in {container_name}. Skipping iperf test.")
        return False

def ping_test(ue_container, target_ip):
    """Run a ping test from a UE container to a target IP."""
    if not target_ip:
        logging.warning(f"Skipping ping from {ue_container}, target IP is None")
        return
    try:
        logging.info(f"Pinging {target_ip} from {ue_container}...")
        result = subprocess.check_output(
            ["/usr/local/bin/docker", "exec", ue_container, "ping", "-c", "4", target_ip],
            stderr=subprocess.STDOUT
        )
        logging.info(f"Ping results from {ue_container} to {target_ip}:\n{result.decode()}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Ping failed from {ue_container} to {target_ip}: {e.output.decode()}")

def run_iperf3_client(client_container, server="test.iperf.org"):
    """Run iperf3 client from a container to test bandwidth."""
    if not check_iperf3_installed(client_container):
        return
    try:
        logging.info(f"Running iperf3 client in {client_container} to {server}...")
        result = subprocess.check_output(
            ["/usr/local/bin/docker", "exec", client_container, "iperf3", "-c", server],
            stderr=subprocess.STDOUT
        )
        logging.info(f"iperf3 results from {client_container} to {server}:\n{result.decode()}")
    except subprocess.CalledProcessError as e:
        logging.error(f"iperf3 client failed from {client_container} to {server}: {e.output.decode()}")

def show_amf_slices_from_logs(amf_container):
    """Fetch and display slices from the AMF container logs."""
    try:
        logging.info(f"Fetching slice information from {amf_container} logs...")
        result = subprocess.check_output(
            ["/usr/local/bin/docker", "exec", amf_container, "grep", "S_NSSAI", "/var/log/open5gs/amf1.log"], 
            stderr=subprocess.STDOUT
        )
        if result:
            logging.info(f"Slice information from {amf_container} logs:\n{result.decode()}")
        else:
            logging.info(f"No slice information found in {amf_container} logs.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error fetching slice info from {amf_container} logs: {e.output.decode()}")
if __name__ == "__main__":
    logging.info("Starting Open5GS and UERANSIM Connectivity Test")

    containers = get_docker_containers()
    
    # Categorize containers correctly
    ue_containers = [c for c in containers if c.startswith("ue")]
    
    core_containers = {
        "amf": None, "smf": None, "upf": None
    }

    for c in containers:
        if "amf" in c:
            core_containers["amf"] = get_container_ip(c)
        elif "smf" in c:
            core_containers["smf"] = get_container_ip(c)
        elif "upf" in c:
            core_containers["upf"] = get_container_ip(c)

    # Select the first available core component (AMF > SMF > UPF)
    target_core_ip = core_containers.get("amf") or core_containers.get("smf") or core_containers.get("upf")

    logging.info(f"UE Containers: {ue_containers}")
    logging.info(f"Core Containers: {core_containers}")

    # Show slices inside AMF containers
    for amf_container in [c for c in containers if "amf" in c]:
        show_amf_slices(amf_container)

    # Run ping tests from each UE to the selected core network element
    if target_core_ip:
        for ue in ue_containers:
            ping_test(ue, target_core_ip)
    else:
        logging.warning("No core network element available for ping test.")

    # Run iperf3 client tests from the core network containers only
    for container in core_containers.values():
        if container:
            run_iperf3_client(container)

    logging.info("Connectivity tests completed.")
