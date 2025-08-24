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

## Project Structure

Self-Healing-Infra/
├── docker-compose.yml
├── prometheus/
│ ├── prometheus.yml
│ └── alert_rules.yml
├── alertmanager/
│ └── alertmanager.yml
├── webhook/
│ └── webhook.py
└── ansible/
├── ansible.cfg
├── inventory
└── restart_nginx.yml
