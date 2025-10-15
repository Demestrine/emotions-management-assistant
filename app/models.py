from app.db import connect_db

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
