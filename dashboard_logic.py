"""
Functions to dynamically update
(1)
How many workouts have been completed and tally them up.

(2)
Streak of back-to-back sessions done.

(3)
Total workout time from all sessions.
"""
from workout_history import *

history_list = WorkoutHistoryList() # creating instance from Class WorkoutHistoryList

def count_total_workouts(history_list):
    if history_list is None:
        return 0 # True so returning 0

    workouts = history_list.get_workouts() # same function name as class method in WorkoutHistory

    if workouts is None:
        return 0

    total_number_of_workouts_completed = len(workouts)
    return total_number_of_workouts_completed


def calculate_current_streak(history_list):
    """
    Streak function:
    I'm leaving this as a placeholder for my teammate to help with.
    """

    return 0

# workout.duration = one workout - how long it lasted
def calculate_total_time_of_all_workouts(history_list):
    if history_list is None:
        return 0

    workouts = history_list.get_workouts()
    if workouts is None or len(workouts) == 0:
        return 0

    total_duration = 0
    for workout in workouts:
        total_duration += workout['duration']

    return total_duration
