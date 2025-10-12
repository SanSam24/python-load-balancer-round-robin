import threading
import time
from flask import Flask, request, Response, jsonify
import requests
import logging
from datetime import datetime
from flask_cors import CORS  # 🔑 for dashboard

app = Flask(__name__)
CORS(app)  # allow cross-origin requests

BACKEND_SERVERS = [
    "http://127.0.0.1:5001",
    "http://127.0.0.1:5002",
    "http://127.0.0.1:5003",
    "http://127.0.0.1:5004",
    "http://127.0.0.1:5005",
    "http://127.0.0.1:5006",
]

active_servers = BACKEND_SERVERS.copy()
counter_lock = threading.Lock()
counter = 0
request_counts = {s: 0 for s in BACKEND_SERVERS}
logs = []

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# 🔹 Health Check
def health_check():
    global active_servers
    while True:
        healthy = []
        for server in BACKEND_SERVERS:
            try:
                res = requests.get(f"{server}/health", timeout=1)
                if res.status_code == 200:
                    healthy.append(server)
            except:
                pass
        active_servers = healthy
        logging.info(f"Active servers: {active_servers}")
        time.sleep(5)

threading.Thread(target=health_check, daemon=True).start()

# 🔹 Proxy / Load Balancer
@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def proxy_request():
    global counter
    if not active_servers:
        return Response("No active servers", status=503)
    with counter_lock:
        server_index = counter % len(active_servers)
        backend_url = active_servers[server_index]
        counter += 1
        request_counts[backend_url] += 1
    start_time = time.time()
    try:
        resp = requests.request(
            method=request.method,
            url=backend_url + request.full_path,
            headers={k:v for k,v in request.headers if k != 'Host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False,
            timeout=3
        )
        latency = round(time.time() - start_time,3)
        logs.append({"timestamp": datetime.now().strftime("%H:%M:%S"),
                     "server": backend_url,
                     "latency": latency})
        logging.info(f"Routed to {backend_url} | Latency: {latency}s | Count: {request_counts[backend_url]}")
        return Response(resp.content, status=resp.status_code, headers=dict(resp.headers))
    except:
        return Response("Backend unreachable", status=502)

# 🔹 /dashboard API
@app.route('/dashboard')
def dashboard():
    summary = {s: request_counts[s] for s in BACKEND_SERVERS}
    recent = logs[-10:]
    avg_latency = round(sum([l['latency'] for l in logs])/len(logs),3) if logs else 0
    return jsonify({
        "active_servers": active_servers,
        "total_requests": sum(request_counts.values()),
        "per_server_requests": summary,
        "average_latency_sec": avg_latency,
        "recent_activity": recent
    })

if __name__ == "__main__":
    print("Load Balancer running on http://127.0.0.1:8080")
    app.run(host='0.0.0.0', port=8080)
