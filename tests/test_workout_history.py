from models.workout_history import WorkoutHistoryList

def test_add_workout():
    history = WorkoutHistoryList()

    history.add_workout("Leg Day")
    history.add_workout("Glutes Day")
    history.add_workout("Arms Day")

    assert history.get_workout()== [
        "Leg Day",
        "Glutes Day",
        "Arms Day"
    ]