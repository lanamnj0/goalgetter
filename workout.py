from db_connection import get_connection


class DbConnectionError(Exception):
    pass

def run_queries(query, params=None):
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

