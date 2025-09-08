from flask import Flask, request
import subprocess, json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    print("Alert received:", json.dumps(data, indent=2))

    for alert in data.get("alerts", []):
        if alert["labels"].get("alertname") == "NginxDown" and data.get("status") == "firing":
            print("Restarting NGINX container with Ansible...")
            subprocess.run([
                "ansible-playbook",
                "ansible/restart_nginx.yml",
                "-i", "ansible/inventory"
            ])
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
