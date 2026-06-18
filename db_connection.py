import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password", # replace with MySQL password
        database="goalgetter"
    )

if __name__ == "__main__":
    connection = get_connection()

    if connection.is_connected():
        print("database successfully connected")

    connection.close()