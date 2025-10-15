from flask import Flask, request, jsonify, render_template, session, redirect, url_for
from models import add_emotion, get_advice_for_emotion
from auth import user_manager
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

@app.route("/")
def home():
    return render_template("index_enhanced.html", user=user_manager.current_user)

@app.route("/analyze", methods=["POST"])
def analyze_emotion():
    emotion = request.form.get("emotion")
    notes = request.form.get("notes", "")
    intensity = request.form.get("intensity", 5, type=int)
    
    if not emotion:
        return render_template("index_enhanced.html", 
                             response="Please enter an emotion.",
                             user=user_manager.current_user)
    
    advice = get_advice_for_emotion(emotion)
    
    # Log emotion if user is logged in
    if user_manager.current_user:
        user_manager.log_emotion(emotion, notes, intensity)
    
    return render_template("index_enhanced.html", 
                         response=advice, 
                         emotion=emotion,
                         user=user_manager.current_user)

@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    email = request.form.get("email", "")
    
    if user_manager.create_user(username, email):
        return redirect(url_for('home'))
    else:
        return render_template("index_enhanced.html", 
                             error="Username already exists",
                             user=user_manager.current_user)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    
    if user_manager.login_user(username):
        return redirect(url_for('home'))
    else:
        return render_template("index_enhanced.html", 
                             error="User not found",
                             user=user_manager.current_user)

@app.route("/logout")
def logout():
    user_manager.current_user = None
    return redirect(url_for('home'))

@app.route("/history")
def emotion_history():
    if not user_manager.current_user:
        return redirect(url_for('home'))
    
    history = user_manager.get_emotion_history()
    return render_template("history.html", 
                         history=history, 
                         user=user_manager.current_user)

@app.route("/export")
def export_data():
    if not user_manager.current_user:
        return redirect(url_for('home'))
    
    history = user_manager.get_emotion_history()
    
    # Create CSV data
    csv_data = "Date,Emotion,Intensity,Notes\\n"
    for emotion, notes, intensity, created_at in history:
        date_str = created_at.strftime("%Y-%m-%d %H:%M")
        csv_data += f'"{date_str}","{emotion}",{intensity},"{notes}"\\n'
    
    return csv_data, 200, {
        'Content-Type': 'text/csv',
        'Content-Disposition': f'attachment; filename=emotion_history_{user_manager.current_user["username"]}.csv'
    }

@app.route("/stats")
def emotion_stats():
    if not user_manager.current_user:
        return redirect(url_for('home'))
    
    history = user_manager.get_emotion_history()
    
    # Calculate basic statistics
    emotion_counts = {}
    total_intensity = 0
    emotion_dates = []
    
    for emotion, notes, intensity, created_at in history:
        emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
        total_intensity += intensity
        emotion_dates.append((emotion, created_at.date()))
    
    avg_intensity = total_intensity / len(history) if history else 0
    most_common = max(emotion_counts.items(), key=lambda x: x[1]) if emotion_counts else ("None", 0)
    
    return render_template("stats.html",
                         emotion_counts=emotion_counts,
                         avg_intensity=round(avg_intensity, 1),
                         most_common=most_common,
                         total_entries=len(history),
                         user=user_manager.current_user)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
