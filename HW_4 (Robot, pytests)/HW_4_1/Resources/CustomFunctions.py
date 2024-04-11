import pyodbc

def connect_to_database_full_way(server, database, username, password, driver="{ODBC Driver 17 for SQL Server}"):
    print(f'Attempting to connect to {server} with user {username}')  # Adding logging
    connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    try:
        connection = pyodbc.connect(connection_string)
        print('Successfully connected to the database')  # Adding logging
        cursor = connection.cursor()
        return cursor
    except Exception as e:
        print(f'Error while connecting to database: {str(e)}')
        return None

def execute_sql_query(cursor, sql_query):
    cursor.execute(sql_query)
    rows = cursor.fetchall()  # get all rows
    if rows:
        return rows
    return []