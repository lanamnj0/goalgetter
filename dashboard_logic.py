"""
Functions to dynamically update
(1)
How many workouts have been completed and tally them up.

(2)
Streak of back-to-back sessions done.

(3)
Total workout time from all sessions.
"""
def calculate_total_workouts(history_list): # Trying to link to singly linked list
    workouts = history_list.get_workouts()
    total_workouts_count = len(workouts)
    return total_workouts_count

def calculate_current_streak(history_list):
    workouts = history_list.get_workouts()
    pass
