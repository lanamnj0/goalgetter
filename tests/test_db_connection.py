import unittest
from unittest.mock import patch 
# import the function being tested
from db_connection import get_connection

# test class for database connection functionality 
class TestDatabaseConnection(unittest.TestCase):
    @patch("db_connection.mysql.connector.connect")

    # test to see if database connection can be established
    def test_uses_environment_configuration(self, mock_connect):
        with patch.dict(
            "os.environ",
            {
                "DB_HOST": "db.example",
                "DB_PORT": "3307",
                "DB_USER": "goalgetter",
                "DB_PASSWORD": "test-password",
                "DB_NAME": "goalgetter_test",
            },
        ):
        
            connection = get_connection()

        self.assertIs(connection, mock_connect.return_value)

        mock_connect.assert_called_once_with(
            host="db.example",
            port=3307,
            user="goalgetter",
            password="test-password",
            database="goalgetter_test",
        )

if __name__ == "__main__":
    unittest.main()