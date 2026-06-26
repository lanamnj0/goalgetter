import unittest
from models.user import User

class TestUser(unittest.TestCase):
    
    def test_create_user_object(self):
        user = User(
            user_id=1,
            username="shalesa",
            email="shalesa@email.com",
            password_hash="password123",
            current_weight_kg=63
            )
        
        self.assertEqual(user.username, "shalesa")
        self.assertEqual(user.email, "shalesa@email.com")
        self.assertEqual(user.current_weight_kg, 63)
        
    def test_hash_password(self):
        user = User(
            1,
            "shalesa",
            "shalesa@email.com",
            "password123",
            63
            )
        
        hashed = user.hash_password("password123")
        self.assertNotEqual(hashed, "password123")
        self.assertEqual(len(hashed), 64)
            
if __name__ == "__main__":
     unittest.main()