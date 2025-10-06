from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Response from Server 1"

if __name__ == "__main__":
    app.run(port=5001)
