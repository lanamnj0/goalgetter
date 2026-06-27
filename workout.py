from db_connection import get_connection


class DbConnectionError(Exception): #empty class for error handlingling and raising exceptions. I can add my custom attribute
    pass

def run_select_queries(query, params=None): #put my db connector and execution code for the select queries into this function for reusability
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

def insert_data_queries(query, params=None): #put my db connector and execution code for insert, update and delete queries into this function for reusability
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


class Workouts(): #created a workout class 
    def __init__(self, user_id, workout_date, duration_minutes, calories_burned, workout_id=None): #class attributes align with the workouts  table in the database
        self.workout_id = workout_id
        self.user_id = user_id
        self.workout_date = workout_date
        self.duration_minutes = duration_minutes
        self.calories_burned = calories_burned