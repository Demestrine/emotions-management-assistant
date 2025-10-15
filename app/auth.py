from db import connect_db
import hashlib
import secrets

class UserManager:
    def __init__(self):
        self.current_user = None
    
    def create_user(self, username, email=None):
        conn = connect_db()
        if not conn:
            return None
        
        cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO users (username, email) VALUES (%s, %s) RETURNING id",
                (username, email)
            )
            user_id = cur.fetchone()[0]
            conn.commit()
            self.current_user = {'id': user_id, 'username': username}
            return self.current_user
        except Exception as e:
            print(f"Error creating user: {e}")
            return None
        finally:
            cur.close()
            conn.close()
    
    def login_user(self, username):
        conn = connect_db()
        if not conn:
            return None
        
        cur = conn.cursor()
        cur.execute("SELECT id, username FROM users WHERE username = %s", (username,))
        user = cur.fetchone()
        cur.close()
        conn.close()
        
        if user:
            self.current_user = {'id': user[0], 'username': user[1]}
            return self.current_user
        return None
    
    def log_emotion(self, emotion_name, notes="", intensity=5):
        if not self.current_user:
            return False
        
        conn = connect_db()
        if not conn:
            return False
        
        cur = conn.cursor()
        try:
            cur.execute(
                """INSERT INTO emotion_history 
                (user_id, emotion_name, notes, intensity) 
                VALUES (%s, %s, %s, %s)""",
                (self.current_user['id'], emotion_name, notes, intensity)
            )
            conn.commit()
            return True
        except Exception as e:
            print(f"Error logging emotion: {e}")
            return False
        finally:
            cur.close()
            conn.close()
    
    def get_emotion_history(self):
        if not self.current_user:
            return []
        
        conn = connect_db()
        if not conn:
            return []
        
        cur = conn.cursor()
        cur.execute(
            """SELECT emotion_name, notes, intensity, created_at 
            FROM emotion_history 
            WHERE user_id = %s 
            ORDER BY created_at DESC""",
            (self.current_user['id'],)
        )
        history = cur.fetchall()
        cur.close()
        conn.close()
        return history

# Global user manager
user_manager = UserManager()
