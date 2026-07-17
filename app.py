import os
import mysql.connector

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.environ.get('DB_HOST'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASSWORD'),
            database=os.environ.get('DB_NAME')
        )
        if connection.is_connected():
            return connection
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Test the connection logic
conn = get_db_connection()
if conn:
    print("SUCCESS: Connected to the database!")
    conn.close()
else:
    print("FAILURE: Could not connect to the database.")