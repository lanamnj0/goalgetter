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


