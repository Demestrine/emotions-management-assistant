from models import add_emotion

print("Updating emotion messages with enhanced professional content...")

# Enhanced, more supportive emotion messages
enhanced_emotions = [
    ("happy", "Embrace this joyful moment. Happiness grows when shared with others. Consider keeping a gratitude journal to prolong these positive feelings."),
    ("sad", "Your feelings are valid and important. Sadness often signals what matters deeply to us. Gentle movement or talking with a trusted friend can help process these emotions."),
    ("anxious", "Anxiety is your body's way of preparing for challenges. Practice grounding techniques: name five things you can see, four you can touch, three you can hear, two you can smell, and one you can taste."),
    ("angry", "Anger often protects deeper feelings. Take space to breathe deeply - inhale for four counts, hold for four, exhale for six. This creates room for thoughtful response."),
    ("excited", "Channel this vibrant energy intentionally. Excitement can fuel meaningful action. Consider what projects or goals could benefit from this enthusiastic drive."),
    ("tired", "Rest is not idleness - it's essential maintenance for your wellbeing. Honor your body's need for recovery. Even brief moments of quiet can be restorative."),
    ("confused", "Uncertainty often precedes new understanding. Break complex situations into smaller, manageable pieces. Sometimes stepping away briefly brings fresh perspective."),
    ("proud", "Acknowledge your achievements fully. Pride in your accomplishments builds self-trust and motivation. Consider what strengths helped you reach this point."),
    ("calm", "Savor this peaceful state. Calmness provides clarity and space for thoughtful decisions. Mindfulness practices can help maintain this balanced perspective."),
    ("stressed", "Stress signals that demands exceed resources. Prioritize what truly matters and delegate when possible. Remember that perfection is less important than progress.")
]

for emotion, advice in enhanced_emotions:
    add_emotion(emotion, advice)
    print(f"Enhanced: {emotion}")

print("Emotion messages updated with professional, supportive content!")
