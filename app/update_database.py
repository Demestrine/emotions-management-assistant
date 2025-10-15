from db import connect_db

def update_schema():
    """Add user accounts and emotion history tables"""
    conn = connect_db()
    if not conn:
        print("Database connection failed")
        return
    
    cur = conn.cursor()
    
    # Create users table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            email VARCHAR(100) UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create emotion_history table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS emotion_history (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            emotion_name VARCHAR(100),
            notes TEXT,
            intensity INTEGER CHECK (intensity >= 1 AND intensity <= 10),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Add some sample users
    cur.execute("INSERT INTO users (username, email) VALUES ('demo_user', 'demo@example.com') ON CONFLICT DO NOTHING")
    
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Database schema updated with users and emotion history tables!")

if __name__ == "__main__":
    update_schema()
