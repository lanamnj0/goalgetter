import unittest
import json
from unittest.mock import patch
from app import app


class WorkoutAPITest(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()


# test for creating workouts
    @patch("app.insert_workouts")
    def test_create_workout_success(self, mock_insert):

        mock_insert.return_value = True

        workout = {
            "user_id": 1,
            "workout_date": "2026-06-25",
            "duration_minutes": 60,
            "calories_burned": 500
        }

        response = self.client.post(
            "/workouts",
            data=json.dumps(workout),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)

    def test_create_workout_missing_field(self):

        workout = {
            "user_id": 1
        }

        response = self.client.post(
            "/workouts",
            data=json.dumps(workout),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)

# test for getting workouts by workout id
    @patch("app.get_workouts_by_id")
    def test_get_workout_success(self, mock_get):

        mock_get.return_value = {
            "workout_id": 1,
            "user_id": 1,
            "duration_minutes": 60,
            "calories_burned": 500
        }

        response = self.client.get("/workouts/1")

        self.assertEqual(response.status_code, 200)

    @patch("app.get_workouts_by_id")
    def test_get_workout_not_found(self, mock_get):

        mock_get.return_value = None

        response = self.client.get("/workouts/99")

        self.assertEqual(response.status_code, 404)

    def test_get_workout_invalid_id(self):

        response = self.client.get("/workouts/abc")

        self.assertEqual(response.status_code, 400)

#  test for getting workouts by user id
    @patch("app.get_workouts_by_user_id")
    def test_get_user_workouts_success(self, mock_get):

        mock_get.return_value = [
            {
                "workout_id": 1,
                "user_id": 1
            }
        ]

        response = self.client.get("/workouts/user/1")

        self.assertEqual(response.status_code, 200)

    @patch("app.get_workouts_by_user_id")
    def test_get_user_workouts_not_found(self, mock_get):

        mock_get.return_value = None

        response = self.client.get("/workouts/user/99")

        self.assertEqual(response.status_code, 404)


# test for updating workouts
    @patch("app.update_workout")
    @patch("app.get_workouts_by_id")
    def test_update_workout_success(self, mock_get, mock_update):

        mock_get.return_value = {
            "workout_id": 1
        }

        mock_update.return_value = True

        update_data = {
            "duration_minutes": 90
        }

        response = self.client.put(
            "/workout/update/1",
            data=json.dumps(update_data),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)

    @patch("app.get_workouts_by_id")
    def test_update_workout_not_found(self, mock_get):

        mock_get.return_value = None

        update_data = {
            "duration_minutes": 90
        }

        response = self.client.put(
            "/workout/update/99",
            data=json.dumps(update_data),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 404)

# test for deleting workouts
    @patch("app.delete_workout")
    @patch("app.get_workouts_by_id")
    def test_delete_workout_success(self, mock_get, mock_delete):

        mock_get.return_value = {
            "workout_id": 1
        }

        mock_delete.return_value = True

        response = self.client.delete("/workout/delete/1")

        self.assertEqual(response.status_code, 200)

    @patch("app.get_workouts_by_id")
    def test_delete_workout_not_found(self, mock_get):

        mock_get.return_value = None

        response = self.client.delete("/workout/delete/99")

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()