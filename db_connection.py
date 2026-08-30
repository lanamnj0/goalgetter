import os 

import mysql.connector
from dotenv import load_dotenv

load_dotenv() 

# connect to the GoalGetter MySQL database using local credentials 
def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "goalgetter"),
    )

if __name__ == "__main__":
    connection = get_connection()

    if connection.is_connected():
        print("database successfully connected")

    # close the database connection after use 
    connection.close()