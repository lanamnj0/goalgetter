from workout import run_select_queries, insert_data_queries, WorkoutExercises, Workouts

def insert_workouts(table, data):
    if table == "workouts":
        query = """INSERT INTO workouts (user_id, workout_date, duration_minutes, calories_burned)
        VALUES (%s, %s, %s, %s)""" 
        insert_data_queries(query, data)
    elif table == "workout_exercises":
        query = """INSERT INTO workout_exercises (workout_id, exercise_id, set_count, reps, weight_kg) VALUES (%s, %s, %s, %s, %s)""" 
        insert_data_queries(query, data)
    
    print("Executed")

def get_workouts_by_id(workout_id,):
    query = """SELECT * FROM workouts WHERE workout_id = %s"""
    return run_select_queries(query, workout_id)

def get_workouts_by_user_id(user_id,):
    query = """SELECT * FROM workouts WHERE user_id = %s"""
    return run_select_queries(query, user_id)  