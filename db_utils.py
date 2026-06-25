from workout import run_select_queries, insert_data_queries, WorkoutExercises, Workouts

# ---------------- INSERT ----------------
def insert_workouts(table, data):
    if table == "workouts":
        query = """INSERT INTO workouts (user_id, workout_date, duration_minutes, calories_burned)
        VALUES (%s, %s, %s, %s)""" 
        insert_data_queries(query, data)
    elif table == "workout_exercises":
        query = """INSERT INTO workout_exercises (workout_id, exercise_id, set_count, reps, weight_kg) VALUES (%s, %s, %s, %s, %s)""" 
        insert_data_queries(query, data)
    
    print("Executed")

# ---------------- GET BY ID ----------------
def get_workouts_by_id(workout_id,):
    query = """SELECT * FROM workouts WHERE workout_id = %s"""
    result = run_select_queries(query, (workout_id,))

    if not result:
        return None

    row = result[0]

    return Workouts(
        workout_id=row["workout_id"],
        user_id=row["user_id"],
        workout_date=row["workout_date"],
        duration_minutes=row["duration_minutes"],
        calories_burned=row["calories_burned"]
    )

# ---------------- GET BY USER ----------------
def get_workouts_by_user_id(user_id,):
    query = """SELECT * FROM workouts WHERE user_id = %s"""
    results = run_select_queries(query, (user_id,))  
    workouts_list = []

    for row in results:
        workout = Workouts(
        workout_id=row["workout_id"],
        user_id=row["user_id"],
        workout_date=row["workout_date"],
        duration_minutes=row["duration_minutes"],
        calories_burned=row["calories_burned"]
    )

    workouts_list.append(workout)

    return workouts_list

# ---------------- UPDATE ----------------
def update_workout(data, workout_id):
    fields = []
    values = []

    allowed_fields = ["user_id", "workout_date", "duration_minutes", "calories_burned"]

    for field in allowed_fields:
        if field in data:
            fields.append(f"{field} = %s")
            values.append(data[field])

    if not fields:
        return None
    
    values.append(workout_id)

    query = f"""UPDATE workouts SET {', '.join(fields)} WHERE workout_id = %s"""

    insert_data_queries(query, values)

    return get_workouts_by_id(workout_id,)

# ---------------- DELETE ----------------
def delete_workout(workout_id):
    insert_data_queries(
        """DELETE FROM workout_exercises WHERE workout_id = %s""",
        (workout_id,)
    )
        
    insert_data_queries("""DELETE FROM workouts WHERE workout_id = %s""", (workout_id,))
    
    return True