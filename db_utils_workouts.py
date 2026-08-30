from workout import run_select_queries, insert_data_queries

# ---------------- INSERT ----------------
def insert_workouts(table, data):
    if table != "workouts": #validates the param table is the database workouts table
        raise ValueError("Unsupported table")

    query = """
        INSERT INTO workouts
        (user_id, workout_date, duration_minutes, calories_burned)
        VALUES (%s, %s, %s, %s)
        """
        
    return insert_data_queries(query, data) #if table is valid then execution of the above query using the database connection function to insert data

# ---------------- GET ALL ----------------
def get_all_workouts():
    return run_select_queries("SELECT * FROM workouts") #gets all workouts

# ---------------- GET BY ID ----------------
def get_workouts_by_id(workout_id,):
    query = """SELECT * FROM workouts WHERE workout_id = %s"""
    result = run_select_queries(query, (workout_id,)) #gets workouts by workout id

    if not result:
        return None #if theres no workout by that id then we return none

    row = result[0] #index 0 because there should only be one workout by that id (its a unique number)

    return (row)

# ---------------- GET BY USER ----------------
#this is part of my hisory page for past workouts
def get_workouts_by_user_id(user_id,):
    query = """SELECT * FROM workouts WHERE user_id = %s""" #getting all past workouts for a specific user
    results = run_select_queries(query, (user_id,))  #this calls the function
    

    return results #return the results in an array.

# ---------------- UPDATE ----------------
def update_workout(data, workout_id):
    fields = []
    values = []

    allowed_fields = ["user_id", "workout_date", "duration_minutes", "calories_burned"]

    for field in allowed_fields: #iterating through allowed field
        if field in data: #checks if the values in allowed field align with those being passed through the data param
            fields.append(f"{field} = %s") #if field is in the data, then we append the field to the fields empty list variable
            values.append(data[field]) #appends the new values being passed through the data param for the column/s (in database) we want to update

    if not fields:
        return None #if the fields is empty then return none
    
    values.append(workout_id) #we then append workout id outside for loop because it is not mutable

    query = f"""UPDATE workouts SET {', '.join(fields)} WHERE workout_id = %s""" #query for updating column values

    insert_data_queries(query, values)

    return get_workouts_by_id(workout_id) #returning the updated workout

# ---------------- DELETE ----------------
def delete_workout(workout_id):
    insert_data_queries(
        """DELETE FROM workout_exercises WHERE workout_id = %s""",
        (workout_id,)
    ) 
        
    insert_data_queries("""DELETE FROM workouts WHERE workout_id = %s""", (workout_id,)) #deleting from both workout and workout exercise tables because they are connected with the foreign key
    
    return True

