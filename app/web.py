from flask import Flask, request, jsonify, render_template
from models import add_emotion, get_advice_for_emotion

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze_emotion():
    emotion = request.form.get("emotion")
    if not emotion:
        return render_template("index.html", response="Please enter an emotion.")
    
    advice = get_advice_for_emotion(emotion)
    return render_template("index.html", response=advice, emotion=emotion)

@app.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    emotion = data.get("emotion")
    advice = data.get("advice")
    add_emotion(emotion, advice)
    return jsonify({"message": f"emotion '{emotion}' added successfully"})

if __name__ == "__main__":
    app.run(debug=True)