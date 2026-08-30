from db_connection import get_connection
from werkzeug.security import generate_password_hash

class User:
    def __init__(
            self,
            user_id,
            username,
            email,
            password_hash,
            current_weight_kg
    ):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.current_weight_kg = current_weight_kg
    
    def hash_password(self, password):
        return generate_password_hash(password)
    
    # CREATE USER PROFILE - adding new user to database

    def create_user(self):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO users
        (username, email, password_hash, current_weight_kg)
        VALUES (%s, %s, %s, %s)
        """
        hashed_password = self.hash_password(self.password_hash)
        values = (
            self.username,
            self.email,
            hashed_password,
            self.current_weight_kg
        )

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

        return "User profile created successfully"

     # GET USER PROFILE DATA - getting/retriving their personal info from SQL databse

    def get_user(self):
        
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT user_id,
           username,
           email,
           current_weight_kg
        FROM users
        WHERE user_id = %s
        """

        cursor.execute(query, (self.user_id, ))
        user = cursor.fetchone()

        cursor.close()
        connection.close()

        return user
        
     # UPDATE USER PROFILE INFO - change a users info/detials

    def update_user(self):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        UPDATE users
         SET username=%s,
         email=%s,
         current_weight_kg=%s

        WHERE user_id=%s
        """
        values = (
            self.username,
            self.email,
            self.current_weight_kg,
            self.user_id
        )
        
        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

        return "User profile updated successfully"

    # DELETE USER PROFILE DATA - remove user from app

    def delete_user(self):

        connection = get_connection()
        cursor = connection.cursor()

        query = """
        DELETE FROM users
        WHERE user_id=%s
        """

        cursor.execute(query, (self.user_id,))

        connection.commit()

        cursor.close()
        connection.close()

        return "User profile has now been deleted"

    # DISPLAY USER PROFILE DATA - display specfic user details that are already stored

    def display_profile(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "current_weight_kg": self.current_weight_kg
        }