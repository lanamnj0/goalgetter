"""
Calendar Breadth First Search logic to calculate weekly schedule - rests vs. workout days for user
"""

from collections import deque

def generate_7_day_schedule():
    # queue (FIFO) storing tuples of variables that are immutable (day_number, consecutive_workouts, current_schedule_list)
    # Start: Day 0, 0 consecutive workout days, empty schedule = []
    queue = deque([(0, 0, [])])

    valid_schedules = []

    while queue:
        # Look at the current state, pop to evaluate/work with it
        day, consecutive, schedule = queue.popleft()

        # If we get to 7 days it should save to the valid_schedules list
        if day == 7:
            valid_schedules.append(schedule)
            continue # we move to the next line of program

        # Adding a Workout day, if we have exercises in two days
        if consecutive < 2:
            queue.append((day + 1, consecutive + 1, schedule + ["Workout🏋️‍♀️ "]))

        # Adding a Rest day ( can always happen, but it does reset the consecutive day streak )
        queue.append((day +1, 0, schedule + ["Rest 💤"]))

    return valid_schedules

def get_first_schedule():
    all_available_schedules = generate_7_day_schedule()
    return all_available_schedules[0] if all_available_schedules else "No schedule currently found"

def get_schedule_for_calendar():
    schedule = get_first_schedule()

    day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    calendar_data = {}

    for i, day in enumerate(schedule): # assigning index to value
        calendar_data[day_names[i]] = day

    return calendar_data

def get_workout_count_from_history(history_list): # Connecting to singly linked list
    if history_list is None:
        return "No history available"

    workouts = history_list.get_workouts()


