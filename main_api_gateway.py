from flask import Flask, jsonify
import requests

app = Flask(__name__)

WORKER_NODES = {
    "VM-2": "http://10.0.2.5:5001/contribution",
    "VM-3": "http://10.0.2.15:5002/contribution"
}

@app.route('/status', methods=['GET'])
def status():
    contributions = []
    for vm, url in WORKER_NODES.items():
        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                contributions.append(response.json())
            else:
                contributions.append({"VM": vm, "Contribution": "Unavailable"})
        except requests.exceptions.RequestException:
            contributions.append({"VM": vm, "Contribution": "Error connecting"})

    return jsonify({"Main VM": "VM-1", "Worker Contributions": contributions})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
