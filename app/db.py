import psycopg2
from psycopg2 import sql
import os

# this function connects to the postgresql database
def connect_db():
    try:
        connection = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", "5432")
        )
        print("connected to the database successfully")
        return connection
    except Exception as e:
        print("database connection failed:", e)
        return None
