"""
Functions to dynamically update
(1)
How many workouts have been completed and tally them up.

(2)
Streak of back-to-back sessions done.

(3)
Total workout time from all sessions.
"""
from models.workout_history import WorkoutHistoryList
from datetime import date, timedelta

def _workouts(history):
    if history is None:
        return [] 

    return history.get_workouts() or [] # creating instance from Class WorkoutHistoryList

def count_total_workouts(history):
    return len(_workouts(history))

# workout.duration = one workout - how long it lasted
def calculate_total_time_of_all_workouts(history):
    return sum(
        workout.get("duration", 0)
        for workout in _workouts(history)
    )


def calculate_current_streak(history, today=None):
    workout_dates = {
        date.fromisoformat(str(workout["date"]))
        for workout in _workouts(history)
        if workout.get("date")
    }

    if not workout_dates:
        return 0 

    current = today or max(workout_dates)
    streak = 0 

    while current in workout_dates:
        streak += 1 
        current -= timedelta(days=1)

    return streak

