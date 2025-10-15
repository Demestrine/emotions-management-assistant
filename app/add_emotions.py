from models import add_emotion

emotions = [
    ("happy", "Keep spreading the joy Gratitude amplifies happiness"),
    ("sad", "Its okay to feel low sometimes Try journaling or taking a short walk"),
    ("anxious", "Breathe in breathe out You are stronger than your worries"),
    ("angry", "Take a deep breath Responding calmly gives you control")
]

for emotion, advice in emotions:
    add_emotion(emotion, advice)
    print(f"Added: {emotion}")

print("All emotions added successfully!")
