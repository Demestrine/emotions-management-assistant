-- this file keeps the database table creation script
CREATE TABLE IF NOT EXISTS emotions (
    id SERIAL PRIMARY KEY,
    emotion_name VARCHAR(100),
    advice TEXT
);
