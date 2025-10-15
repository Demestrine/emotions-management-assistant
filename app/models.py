from db import connect_db

# this function creates the table for storing emotions
def create_emotions_table():
    connection = connect_db()
    if not connection:
        return
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS emotions (
            id SERIAL PRIMARY KEY,
            emotion_name VARCHAR(100),
            advice TEXT
        );
    ''')
    connection.commit()
    cursor.close()
    connection.close()
    print("emotions table created successfully")

# this function adds a new emotion and its advice
def add_emotion(emotion_name, advice):
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO emotions (emotion_name, advice) VALUES (%s, %s);",
        (emotion_name, advice)
    )
    connection.commit()
    cursor.close()
    connection.close()
    print(f"added emotion: {emotion_name}")

# this function gets advice for a specific emotion
def get_advice_for_emotion(emotion_name):
    connection = connect_db()
    if not connection:
        return "Database connection failed. Please try again."
    
    cursor = connection.cursor()
    cursor.execute(
        "SELECT advice FROM emotions WHERE emotion_name = %s;",
        (emotion_name.lower(),)
    )
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    
    if result:
        return result[0]
    else:
        return "I understand you're feeling that way. Remember, it's okay to experience different emotions. 💙"
