import unittest
from calendar_logic import generate_7_day_schedule
from collections import deque

# Mocking functions to test it
def validate_workout_limit(consecutive_days):
    if consecutive_days >= 2:
        return "Force Rest Day"
    return "Allow for Workout Day"

def calculate_weekly_schedule(days):
    if days == 7:
        return "Week complete! (saving to schedule)"
    elif days <= 2:
        return "Getting there!"
    return "Days of the week not yet configured"

# Mocked data class to figure out testing logic
class TestMockedCalendarLogic(unittest.TestCase):
    # Valid unittest case
    def test_overwork_logic_valid(self):
        mock_consecutive_days = 2
        expected_result = "Force Rest Day"

        actual_result = validate_workout_limit(mock_consecutive_days)

        self.assertEqual(expected_result, actual_result) # Accepted

    # Valid edge/boundary case
    def test_schedule_valid_boundary(self):
        mock_days = 2 # exactly at the boundary, could also test '7'
        expected_result = "Getting there!"

        actual_result = calculate_weekly_schedule(mock_days)

        self.assertEqual(expected_result, actual_result)

    # Invalid edge/boundary case
    def test_weekly_schedule_invalid_boundary(self): # above the set boundary
        mock_days = 8 # Upper boundary set to 7
        expected_result = ("Week complete! (saving to schedule)"  or "Getting there!")

        actual_result = calculate_weekly_schedule(mock_days)

        self.assertEqual(expected_result, actual_result) # Neither conditions accepted since it is an invalid boundary

    # Invalid case
    def test_workout_limit_invalid(self):
        mock_consecutive_days = "3" # Deliberately wrong datatype
        expected_result = "Allow for Workout Day"

        actual_result = validate_workout_limit(mock_consecutive_days)

        self.assertEqual(expected_result, actual_result) # Test fails as intended, it should return "Force Rest day"

# Checking for validity in the function created
class TestCalendarLogic(unittest.TestCase):
    def test_generate_7_day_schedule_result_type_valid(self):
        actual_result = generate_7_day_schedule()

        self.assertIsInstance(actual_result, list) # Should return a list of the schedule

    def test_generate_7_day_schedule_week_created_valid(self):
        actual_result = generate_7_day_schedule()

        for schedule in actual_result:
            self.assertEqual(len(schedule), 7) # Checking that it has created a 7-day schedule

    def test_generate_7_day_schedule_no_three_workouts_valid(self):
        actual_result = generate_7_day_schedule()

        for schedule in actual_result:
            # Check each schedule for "Workout" repeated 3 times
            for i in range(len(schedule) - 2):
                self.assertNotEqual(
                    (schedule[i], schedule[i + 1], schedule[i + 2]),
                    ('Workout', 'Workout', 'Workout')
                )

if __name__ == '__main__':
    unittest.main()
