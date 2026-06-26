import unittest
# import the function being tested
from db_connection import get_connection

# test class for database connection functionality 
class TestDatabaseConnection(unittest.TestCase):

    # test to see if database connection can be established
    def test_connection_exists(self):
        connection = get_connection()

        self.assertIsNotNone(connection)

        connection.close()

    # test to see if the application connects to the correct database
    def test_database_name(self):
        connection = get_connection()

        self.assertEqual(connection.database, "goalgetter")

        connection.close()

if __name__ == "__main__":
    unittest.main()