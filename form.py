import sqlite3

def create_database():
    conn = sqlite3.connect('Form.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student (
            Fullname TEXT,
            Email TEXT,
            Gender TEXT,
            Country TEXT,
            Programming TEXT
        )
    ''')
    
    
    conn.commit()
    conn.close()


create_database()

print("Database and table created successfully!")
