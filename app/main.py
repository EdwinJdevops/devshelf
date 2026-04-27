from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return {"status": "DevShelf GitOps Engine - Live", "version": "1.0.0"}

@app.route("/health")
def health():
    return {"health": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
