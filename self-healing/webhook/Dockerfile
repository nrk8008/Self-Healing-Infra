FROM python:3.12-slim

WORKDIR /app

# Copy webhook script and Ansible files
COPY webhook.py /app/webhook.py
COPY ansible /app/ansible

# Install dependencies
RUN pip install flask ansible

EXPOSE 5001

CMD ["python", "webhook.py"]
