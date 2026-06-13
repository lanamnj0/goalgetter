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
    
    def create_user(self):
        """"Create a new user in the database"""
        pass

    def get_user(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "email": self.email,
            "password_hash": self.password_hash,
            "current_weight_kg": self.current_weight_kg
        }

    def update_user(self):
        """"Update user details"""
        pass

    def delete_user(self):
        """"Delete a user from database"""
        pass

    def display_profile(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "current_weight_kg": self.current_weight_kg
        }