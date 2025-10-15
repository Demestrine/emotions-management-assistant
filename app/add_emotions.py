from models import add_emotion

def add_natural_emotions():
    natural_emotions = [
        ("happy", "That's wonderful to hear! When I feel happy, I try to really soak in the moment. Maybe share that good energy with someone who could use it today."),
        ("sad", "I get that. Some days just feel heavy. When I'm down, making a warm drink and putting on comfortable clothes helps. Or just letting myself be sad for a bit - it usually passes."),
        ("anxious", "Ugh, anxiety is the worst. I find counting breaths helps - four in, hold four, six out. Or naming things around me: five things I see, four I can touch... it grounds me."),
        ("angry", "Anger is tough. I usually need to step away for a minute - maybe splash some cold water on my face. Giving myself space to cool down helps me respond instead of react."),
        ("excited", "That's awesome! That buzzing energy is great for getting things done. I'd use it to tackle something you've been putting off - that excitement can be contagious!"),
        ("tired", "I hear you. Sometimes our bodies just need a break. Even 10 minutes of quiet or a short walk can help reset things. No shame in resting - we're human, not machines."),
        ("confused", "Confusion is just your brain processing new information. I find it helps to break things into smaller pieces or talk it out with someone. Usually clarity comes with time."),
        ("proud", "You should feel proud! Recognizing your own achievements is important. Maybe take a moment to really acknowledge what you did - we often rush past these moments."),
        ("calm", "That peaceful feeling is so nice. I try to extend those moments by just breathing and being present. It's like charging your batteries for when things get hectic."),
        ("stressed", "Stress makes everything feel urgent. I've learned to ask: what actually needs to happen right now? Often, just one small step forward breaks that overwhelmed feeling."),
        ("bored", "Boredom can be surprisingly useful - it's when I get my most random creative ideas. Sometimes I just lean into it and see what my mind comes up with."),
        ("lonely", "Loneliness hits hard sometimes. Reaching out to someone - even just a quick text - often helps. Or going somewhere public like a coffee shop, just to be around people."),
        ("grateful", "Gratitude changes everything for me. I sometimes write down three small things I appreciated today - a good meal, a funny moment, anything. It adds up."),
        ("hopeful", "Hope is powerful. I find it helps to picture what I'm hoping for in detail, then take one tiny step toward it. Momentum builds from small starts."),
        ("jealous", "Jealousy usually shows me what I actually want. Instead of focusing on others, I ask: what part of that could I create in my own life, in my own way?"),
        ("guilty", "Guilt means you care about doing the right thing. If you need to make amends, do it. Then forgive yourself - we all mess up sometimes."),
        ("embarrassed", "Oh I've been there! Most people are too busy thinking about themselves to remember our awkward moments. This will probably be funny in a week."),
        ("confident", "Confidence feels great! Trust that feeling - you've probably earned it through hard work or experience. Let it guide your next moves."),
        ("overwhelmed", "When everything feels like too much, I pick one small thing I can finish. Just completing something - anything - usually makes the rest feel more manageable."),
        ("peaceful", "Peace is precious. I try to notice what created this feeling - was it quiet, nature, company? Remembering that helps me find it again later."),
        ("frustrated", "Frustration usually means I need a different approach. Taking a quick break often helps - when I come back, I see solutions I missed before."),
        ("nostalgic", "Nostalgia is bittersweet. I let myself enjoy the memories, then look for ways to bring what I loved about those times into my present life."),
        ("surprised", "Surprises shake things up! Even unexpected ones often lead somewhere interesting. I try to stay curious about where this might go."),
        ("disappointed", "Disappointment stings. I acknowledge the feeling, then look for what's still possible. Sometimes Plan B turns out better than Plan A."),
        ("content", "Contentment is underrated! Soaking in these satisfied moments builds resilience for tougher times. Enjoy it while it lasts."),
        ("energetic", "That energetic buzz is perfect for getting things done! I'd use it on something challenging - that energy can power through obstacles."),
        ("playful", "Playfulness is good for the soul! It reminds me not to take everything so seriously. A little silliness can reset a whole day."),
        ("romantic", "Romantic feelings make everything feel more meaningful. Whether it's about a person or a passion, that intensity can inspire beautiful things."),
        ("silly", "Silliness is medicine! Laughing at myself or with others always lifts my mood. Life's too short to be serious all the time."),
        ("victorious", "You did it! Savor that winning feeling - you earned it. These moments fuel us for the next challenge.")
    ]
    
    for emotion, advice in natural_emotions:
        add_emotion(emotion, advice)
        print(f"Added natural: {emotion}")

def clear_existing_emotions():
    """Clear existing emotions to avoid duplicates"""
    from db import connect_db
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM emotions")
    conn.commit()
    cur.close()
    conn.close()
    print("Cleared existing emotions")

def main():
    print("Emotion Management Assistant - Natural Message Setup")
    print("This will replace ALL existing emotions with natural, human-sounding messages")
    
    confirm = input("Continue? This will delete existing emotions (y/n): ")
    if confirm.lower() == 'y':
        clear_existing_emotions()
        add_natural_emotions()
        print("All emotions updated with natural, human-sounding messages!")
    else:
        print("Cancelled - no changes made")

if __name__ == "__main__":
    main()
