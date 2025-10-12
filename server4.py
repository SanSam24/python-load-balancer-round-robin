from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello from Server 4"
@app.route("/health")
def health():
    return "OK", 200
if __name__ == "__main__":
    app.run(port=5004)