# Self-Healing Infrastructure with Prometheus, Alertmanager & Ansible

## Objective
Build a **self-healing infrastructure** that automatically detects when a service (NGINX) goes down or CPU usage exceeds a threshold, and **recovers it automatically** using **Prometheus, Alertmanager, and Ansible**.

---

## Tech Stack
- [Prometheus](https://prometheus.io/) → metrics collection & alerting
- [Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/) → routes alerts to automation
- [Node Exporter](https://github.com/prometheus/node_exporter) → system metrics (CPU, memory)
- [Blackbox Exporter](https://github.com/prometheus/blackbox_exporter) → HTTP probe to monitor NGINX
- [Ansible](https://www.ansible.com/) → automation to restart service
- [Python Flask](https://flask.palletsprojects.com/) → webhook receiver from Alertmanager
- [Docker](https://www.docker.com/) → runs all services in containers
- Sample service: **NGINX**

---

## Features
- Monitors NGINX endpoint uptime (`http://localhost:8080`)
- Monitors CPU usage via Node Exporter
- Sends alerts when:
  - NGINX is unreachable for 30s
  - CPU usage > 90% for 2 minutes
- **Auto-heals** NGINX by restarting the container with Ansible when alert fires

---

## Start Sample Service (NGINX)

    docker run -d --name mynginx -p 8080:80 nginx

## Start Monitoring Stack

    docker compose up -d

- Prometheus → http://localhost:9090

- Alertmanager → http://localhost:9093

- Node Exporter → http://localhost:9100

- Blackbox Exporter → http://localhost:9115

## Install Dependencies (Python + Ansible)

    pip install flask ansible

## Run Webhook Listener

    cd webhook
    python3 webhook.py

Runs on → http://localhost:5001

## Ansible Playbook (Auto-Heal)


## Now everything is working:
### Check everything is running
Run:

      docker ps

Expected: mynginx (nginx) → running on port 8080

- NGINX (mynginx) is up and serving on http://localhost:8080

- Prometheus → http://localhost:9090

- Alertmanager → http://localhost:9093

- Node Exporter → http://localhost:9100/metrics

- Blackbox Exporter → http://localhost:9115

## Test Self-Healing

- Stop NGINX (simulate failure):

      docker stop mynginx


- Wait ~30–60 seconds. What should happen:

      - Prometheus detects probe_success=0.

      - Alertmanager fires NginxDown alert.

      - Webhook receives the alert.

      - Ansible playbook restarts the mynginx container automatically.

- Verify NGINX is restarted:

      docker ps
      curl localhost:8080

