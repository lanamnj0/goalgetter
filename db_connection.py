import mysql.connector

# connect to the GoalGetter MySQL database using local credentials 
def get_connection():
    print("USING UPDATED CONNECTION FILE") 
    return mysql.connector.connect(
        host="localhost",
        user="python_user",
        password="password123", # replace with your local MySQL password
        database="goalgetter"
    )
if __name__ == "__main__":
    connection = get_connection()

    if connection.is_connected():
        print("database successfully connected")

    # close the database connection after use 
    connection.close()