import sqlite3

def create_database():
    # Create a connection to the database (it will create the file if it doesn't exist)
    conn = sqlite3.connect('Form.db')
    
    # Create a cursor object
    cursor = conn.cursor()
    
    # Create the Student table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student (
            Fullname TEXT,
            Email TEXT,
            Gender TEXT,
            Country TEXT,
            Programming TEXT
        )
    ''')
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()

# Call the function to create the database and table
create_database()

print("Database and table created successfully!")
