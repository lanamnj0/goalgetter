import mysql.connector

# connect to the GoalGetter MySQL database using local credentials
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password_here", # replace with your local MySQL password
        database="goalgetter"
    )

if __name__ == "__main__":
    connection = get_connection()

    if connection.is_connected():
        print("database successfully connected")

    # close the database connection after use
    connection.close()