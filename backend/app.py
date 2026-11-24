from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "CollecBuy",
        "message": "Welcome to CollecBuy API!",
        "status": "running",
        "version": "1.0.0"
    })

@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "CollecBuy Backend"
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)