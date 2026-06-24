from db_connection import get_connection


class DbConnectionError(Exception):
    pass

def run_select_queries(query, params=None):
    db_connection = None
    results = None
    try:
        with get_connection() as db_connection:
            cursor = db_connection.cursor(dictionary=True)
            print("Connecting to database...")
            cursor.execute(query, params)
            print("Executing query...")
            results = cursor.fetchall()
            print("Generating results...")
        for row in results:
            print(row)
        cursor.close()
   
    except Exception:
        raise DbConnectionError(("The database connection failed...Check you have the correct information"), 500)
    
    return results

def insert_data_queries(query, params=None):
    db_connection = None
   
    try:
        with get_connection() as db_connection:
            cursor = db_connection.cursor(dictionary=True)
            print("Connecting to database...")
            cursor.execute(query, params)
            print("Executing query...")
            db_connection.commit()
            print("Insert complete")
            cursor.close()
    
    except Exception:
        raise DbConnectionError(("The database connection failed...Check you have the correct information"), 500)
    
    return (cursor.rowcount)

class WorkoutExercises():
    def __init__(self, workout_id, exercise_id, set_count, reps, weight_kg, id=None):
        self.id = id
        self.workout_id = workout_id
        self.exercise_id = exercise_id
        self.set_count = set_count
        self.reps = reps
        self.weight_kg = weight_kg

class Workouts():
    def __init__(self, user_id, workout_date, duration_minutes, calories_burned, workout_id=None):
        self.workout_id = workout_id
        self.user_id = user_id
        self.workout_date = workout_date
        self.duration_minutes = duration_minutes
        self.calories_burned = calories_burned