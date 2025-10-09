import threading
from flask import Flask, request, Response
import requests
import logging

app = Flask(__name__)

# List of backend servers (easy to add/remove)
BACKEND_SERVERS = [
    "http://127.0.0.1:5001",
    "http://127.0.0.1:5002",
    "http://127.0.0.1:5003",
    "http://127.0.0.1:5004",
    "http://127.0.0.1:5005",
    "http://127.0.0.1:5006",
]

counter_lock = threading.Lock()
counter = 0

# Optional: track per-server request counts
request_counts = [0 for _ in BACKEND_SERVERS]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def proxy_request():
    global counter

    with counter_lock:
        server_index = counter % len(BACKEND_SERVERS)
        backend_url = BACKEND_SERVERS[server_index]
        counter += 1
        request_counts[server_index] += 1

    logging.info(f"Routing request to {backend_url} (Server {server_index+1}), Request count: {request_counts[server_index]}")

    try:
        # Forward the request to the backend server
        backend_response = requests.request(
            method=request.method,
            url=backend_url + request.full_path,
            headers={key: value for key, value in request.headers if key != 'Host'},
            data=request.get_data(),
            cookies=request.cookies,
            allow_redirects=False,
            timeout=3,
        )
        response = Response(
            backend_response.content,
            status=backend_response.status_code,
            headers=dict(backend_response.headers)
        )
        return response
    except requests.exceptions.RequestException as e:
        logging.error(f"Error forwarding to {backend_url}: {e}")
        return Response("Backend server unreachable", status=502)

@app.route('/stats')
def stats():
    stats_text = ""
    for idx, count in enumerate(request_counts):
        stats_text += f"Server {idx+1}: {count} requests\n"
    return "<pre>" + stats_text + "</pre>"

if __name__ == "__main__":
    print("Load Balancer running on http://127.0.0.1:6000")
    app.run(port=8080)