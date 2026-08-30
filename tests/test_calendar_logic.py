import unittest

from calendar_logic import (
    generate_7_day_schedule,
    get_schedule_for_calendar,
)

# Checking for validity in the function created
class TestCalendarLogic(unittest.TestCase):
    def test_generate_complete_weeks(self):
        schedules = generate_7_day_schedule() 

        self.assertGreater(len(schedules), 0)
        self.assertTrue(
            all(len(schedule) == 7 for schedule in schedules)
        )

    def test_never_schedules_three_consecutive_workouts(self):
        for schedule in generate_7_day_schedule():
            workout_days = [
                entry.startswith("Workout")
                for entry in schedule
            ]

            for index in range(len(workout_days) - 2):
                self.assertFalse(
                    all(workout_days[index:index + 3])
                )

    def test_calendar_contains_all_weekdays(self):
        calendar = get_schedule_for_calendar()

        self.assertEqual(
            list(calendar),
            ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        )

if __name__ == '__main__':
    unittest.main()
