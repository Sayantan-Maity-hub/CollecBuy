from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={
    r"/api/*":{
        "origins": "http://localhost:5173"
    }
})

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