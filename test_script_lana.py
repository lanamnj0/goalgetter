from exercise_api import ExerciseAPI

api = ExerciseAPI()

try:
    results = api.search_by_body_part("Shoulders")

    for exercise in results[:5]:
        print("\n----------------------")
        print(f"Workouts for {exercise.get('name', 'exercise')}")
        print("\n----------------------")
        print("ID: ", exercise["exerciseId"])
        print("Exercise Type: ", exercise["exerciseType"])
        print("Image URL: ", exercise["imageUrl"])
        print("Target Muscles: ", exercise["targetMuscles"])
        print("Equipments: ", exercise["equipments"])
        print("Secondary Muscles: ", exercise["secondaryMuscles"])

except Exception as e:
    print("API Failed: ", e)
