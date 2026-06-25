# === IMPORTING MODULES ===
import unittest 
from unittest.mock import patch
from app import create_app

class TestExerciseRoutes(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client() 

    @patch("app.ExerciseAPI")
    def test_exercise_route_body_part(self, mock_api_class):
        mock_api = mock_api_class.return_value 

        mock_api.search_by_body_part.return_value = [
            {
                "exerciseId": "123",
                "name": "Bench Press",
                "exerciseType": "STRENGTH",
                "imageUrl": "image.jpg",
                "targetMuscles": ["PECTORALS"],
                "bodyParts": ["CHEST"],
                "equipments": ["BARBELL"],
                "secondaryMuscles": ["TRICEPS"]
            }
        ]

        response = self.client.get("/exercises?body_part=CHEST")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Bench Press", response.data)
        mock_api.search_by_body_part.assert_called_once_with("CHEST")