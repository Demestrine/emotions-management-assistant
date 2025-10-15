from flask import Flask, request, jsonify
from app.models import add_emotion

# this file will later help to turn the project into a web app using flask
app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "welcome to the emotion management assistant"})

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    emotion = data.get("emotion")
    advice = data.get("advice")
    add_emotion(emotion, advice)
    return jsonify({"message": f"emotion '{emotion}' added successfully"})

if __name__ == "__main__":
    app.run(debug=True)
