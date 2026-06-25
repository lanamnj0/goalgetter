#  Mock API test for the ExerciseAPI external API running 

# === IMPORTING MODULES ===
import unittest 
from unittest.mock import patch
from exercise_api import ExerciseAPI 

# TEST - searching by body part:

class TestExerciseAPI(unittest.TestCase):
    @patch("exercise_api.requests.get")
    def test_search_by_body_part(self, mock_get):

        mock_get.return_value.json.return_value = {
            "data": [
                {
                    "exerciseId": "123",
                    "name": "Bench Press",
                    "exerciseType": "STRENGTH",
                    "imageUrl": "image.jpg", 
                    "targetMuscles": ["PECTORALIS"],
                    "bodyParts": ["CHEST"],
                    "equipments": ["BARBELL"],
                    "secondaryMuscles": ["TRICEPS"]

                },
                {
                    "exerciseId": "456",
                    "name": "Squat",
                    "bodyParts": ["THIGHS"],
                    "targetMuscles": ["QUADRICEPS"],
                    "equipments": ["BARBELL"],
                }
            ]
        }

        mock_get.return_value.raise_for_status.return_value = None 

        api = ExerciseAPI()
        results = api.search_by_body_part("CHEST")

        self.assertEqual(len(results), 2)
        self.assertEqual(results[0]["name"], "Bench Press")
        self.assertIn("CHEST", results[0]["bodyParts"])