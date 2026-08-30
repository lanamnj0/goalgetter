from db_connection import get_connection


class DbConnectionError(RuntimeError): #empty class for error handlingling and raising exceptions. I can add my custom attribute
    pass

def run_select_queries(query, params=None): #put my db connector and execution code for the select queries into this function for reusability
    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(query, params or ())
            return cursor.fetchall()
        finally:
            cursor.close()
            connection.close()
   
    except Exception as exc:
        raise DbConnectionError("The database query failed.") from exc
    
def insert_data_queries(query, params=None): #put my db connector and execution code for insert, update and delete queries into this function for reusability
   
    try:
        connection = get_connection()
        cursor = connection.cursor() 

        try:
            cursor.execute(query, params or ())
            connection.commit()
            return cursor.rowcount
        except Exception:
            connection.rollback() 
            raise

        finally:
            cursor.close()
            connection.close() 

    except Exception as exc:
        raise DbConnectionError("The database update failed") from exc



