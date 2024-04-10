import pyodbc
import pytest
from credentials import *


class SQLConnect:
    def __init__(self, server=None, database=None, username=None, password=None,
                 driver="{ODBC Driver 17 for SQL Server}"):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.driver = driver
        self.connection = None
        self.cursor = None

        try:
            self.connection = pyodbc.connect(server=server, database=database, user=username,
                                             password=password, driver=driver)
            self.cursor = self.connection.cursor()
            print('Successfully connected to the database')  # Adding logging
        except Exception as e:
            print(f'Error while connecting to database: {str(e)}')

    def execute_sql_query(self, query):
        # execute query and return 1 row
        self.cursor.execute(query)
        return self.cursor.fetchone()


@pytest.fixture(scope="session")
def db():
    return SQLConnect(server, database, user, password, driver)
