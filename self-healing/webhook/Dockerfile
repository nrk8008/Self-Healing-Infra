FROM python:3.12-slim

WORKDIR /app

# Copy webhook and Ansible files
COPY webhook.py /app/webhook.py
COPY ansible /app/ansible

# Install dependencies for Ansible and Docker modules
RUN apt-get update && apt-get install -y --no-install-recommends \
    sshpass \
    openssh-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
RUN pip install --upgrade pip \
    && pip install flask ansible requests docker community.docker

EXPOSE 5001

CMD ["python", "webhook.py"]
