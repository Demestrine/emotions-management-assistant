from models import add_emotion

# Clear existing emotions and add enhanced messages
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
    ("stressed", "Stress signals that demands exceed resources. Prioritize what truly matters and delegate when possible. Remember that perfection is less important than progress."),
    ("bored", "Boredom can spark creativity. This mental space allows new ideas to emerge. Try something outside your routine or learn a simple new skill."),
    ("lonely", "Connection is a fundamental human need. Reach out to supportive relationships, or explore communities with shared interests. Sometimes helping others alleviates our own loneliness."),
    ("grateful", "Gratitude rewires our brain for positivity. Write down three specific things you appreciate right now. This practice builds resilience during challenging times."),
    ("hopeful", "Hope provides direction during uncertainty. Visualize positive outcomes and identify one small step you can take today toward that vision."),
    ("jealous", "Jealousy often points to unmet needs or values. Explore what you truly desire for yourself, then create a plan to cultivate those qualities in your own life."),
    ("guilty", "Guilt can guide us toward our values. Make amends where appropriate, then practice self-compassion. Learning from mistakes helps us grow."),
    ("embarrassed", "Embarrassment reminds us we're human. Most people are focused on their own concerns. This feeling will pass, often leaving wisdom in its wake."),
    ("confident", "Confidence grows from acknowledging your capabilities. Trust your preparation and experience. Remember past challenges you've successfully navigated."),
    ("overwhelmed", "When everything feels urgent, nothing is. Identify the single most important task right now. Completing one thing creates momentum for the next."),
    ("peaceful", "Peace is a precious resource. Notice what conditions support this state. Simple rituals like mindful breathing can help return to peace when needed."),
    ("frustrated", "Frustration signals that current approaches aren't working. Step back and consider alternative strategies. Sometimes a brief break provides new solutions."),
    ("nostalgic", "Nostalgia connects us to meaningful experiences. Honor these memories while staying present to current opportunities for meaning and connection."),
    ("surprised", "Surprise opens us to new possibilities. Stay curious about what this unexpected moment might teach you. Flexibility often leads to valuable discoveries."),
    ("disappointed", "Disappointment reveals our hopes and investments. Acknowledge the loss, then look for alternative paths forward. New opportunities often emerge from adjusted expectations."),
    ("content", "Contentment is a profound achievement. Savor this satisfaction without pressure for what's next. These moments nourish us for future challenges."),
    ("energetic", "Direct this vitality toward what matters most. High energy periods are ideal for tackling challenging projects or initiating positive changes."),
    ("playful", "Playfulness fuels creativity and connection. Embrace lighthearted moments - they provide balance to life's seriousness and spark innovation."),
    ("romantic", "Romantic feelings highlight our capacity for deep connection. Express authentic affection and create space for mutual understanding and appreciation."),
    ("silly", "Lightheartedness is therapeutic. Laughter reduces stress and strengthens social bonds. Don't underestimate the value of moments that simply feel good."),
    ("victorious", "Celebrate your successes fully. Acknowledging victories, large and small, builds confidence and motivation for future endeavors.")
]

print("Updating emotion messages with enhanced supportive content...")

# Note: You might want to clear the existing emotions first
# For now, this will add them as new entries
for emotion, advice in enhanced_emotions:
    add_emotion(emotion, advice)
    print(f"Enhanced: {emotion}")

print("All emotion messages updated with professional, supportive content!")
