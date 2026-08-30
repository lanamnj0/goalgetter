from exercise_api import ExerciseAPI

def print_exercises(results, limit=5):
    """
    This function is a reusable display function - we pass in any
    list of formatted exercsie dicts for example a search_by.. method
    and it will print it the same way each time. 

    Limit default = 5 but can be changed when needed. 
    """
    for exercise in results[:limit]:
        print("\n----------------------")
        print(f"Workouts for {exercise.get('name', 'exercise')}")
        print("\n----------------------")
        print("ID: ", exercise.get("exerciseId"))
        print("Exercise Type: ", exercise.get("exerciseType"))
        print("Image URL: ", exercise.get("imageUrl"))
        print("Target Muscles: ", exercise.get("targetMuscles"))
        print("Equipments: ", exercise.get("equipments"))
        print("Secondary Muscles: ", exercise.get("secondaryMuscles"))

print_exercises() 
