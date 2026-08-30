import unittest
from dashboard_logic import calculate_total_time_of_all_workouts, count_total_workouts
from models.workout_history import WorkoutHistoryList

"""
Tests widget functionality
"""

class TestWidgetFunctions(unittest.TestCase):
    def test_count_workouts_with_real_list_valid(self):
        history = WorkoutHistoryList()

        #  Adding mock workouts to it, each workout is a dictionary (or object) with duration and date
        workout1 = {"duration": 30, "date": "2026-06-20"}
        workout2 = {"duration": 45, "date": "2026-06-21"}
        workout3 = {"duration": 20, "date": "2026-06-22"}

        history.add_workout(workout1)
        history.add_workout(workout2)
        history.add_workout(workout3)

        result = count_total_workouts(history)

        self.assertEqual(result, 3)

    def test_total_time_valid(self):
        history = WorkoutHistoryList() # Creating instance
        workout1 = {"duration": 30, "date": "2026-06-20"}
        workout2 = {"duration": 45, "date": "2026-06-21"}
        workout3 = {"duration": 20, "date": "2026-06-22"} # Nodes created
        history.add_workout(workout1)
        history.add_workout(workout2)
        history.add_workout(workout3) # Added to linked list

        result = calculate_total_time_of_all_workouts(history)
        self.assertEqual(result, 95) # 30 + 45 + 20 = 95


    def test_total_time_invalid_boundary(self):
        result = calculate_total_time_of_all_workouts(None)
        self.assertEqual(result, 0) # its on the boundary, but not a case that would be valid for functionality.

    def test_count_workouts_empty_list_invalid(self):
        history = WorkoutHistoryList()
        result = count_total_workouts(history)
        self.assertEqual(result, 0) # Shouldn't be empty - means we have no data stored

if __name__ == '__main__':
    unittest.main()
