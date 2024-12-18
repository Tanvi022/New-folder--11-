import sqlite3

def create_database():
    conn = sqlite3.connect('Form.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student (
            Fullname TEXT,
@@ -18,11 +13,11 @@ def create_database():
        )
    ''')
    conn.commit()
    conn.close()

create_database()

print("Database and table created successfully!")

