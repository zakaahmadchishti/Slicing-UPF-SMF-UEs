# Use a lightweight Python image
FROM python:3.9-slim

# Install Docker CLI and Docker Compose, log installation times
RUN apt-get update && apt-get install -y \
    ca-certificates \
    curl \
    lsb-release \
    gnupg \
    && echo "Docker installation started at $(date)" \
    && curl -fsSL https://get.docker.com -o get-docker.sh \
    && sh get-docker.sh \
    && rm get-docker.sh \
    && curl -L "https://github.com/docker/compose/releases/download/v2.6.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose \
    && echo "Docker installation completed at $(date)"

# Set the working directory inside the container
WORKDIR /app

# Copy the Flask webhook script into the container
COPY webhook_listener.py /app/webhook_listener.py

# Install Flask and requests, log installation times
RUN echo "Flask and requests installation started at $(date)" \
    && pip install Flask requests \
    && echo "Flask and requests installation completed at $(date)"

# Expose the port the webhook service will listen on
EXPOSE 5001

# Define the command to run when the container starts
CMD ["sh", "-c", "echo 'nameserver 8.8.8.8' > /etc/resolv.conf && \
    echo 'nameserver 8.8.4.4' >> /etc/resolv.conf && \
    python /app/webhook_listener.py"]