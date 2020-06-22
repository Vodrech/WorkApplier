import sqlite3 as sql
import Database.ManagerDB as DB

"""

Handles all the injections to the database

"""


class SQL:

    def __init__(self):
        self.database = DB.DB()
        self.connection_string = self.database.pathway + self.database.file_name + '.db'

    def create_connection(self):

        try:
            conn = sql.connect(self.connection_string)
            return conn

        except ConnectionError as e:
            ConnectionError('Connection between sqlite could not be established, please see error', e)

    def create_table(self):

        injection = """ CREATE TABLE IF NOT EXISTS data 
        (workplace text NOT NULL, worktitle text, applied integer DEFAULT 0"""

        try:
            connection = self.create_connection()
            connection.cursor().execute(injection)
        except Exception as e:
            Exception('Could not create the database table, please check error log', e)

    # Applies to a workplace
    def apply(self, workplace):

        injection = ("""UPDATE data SET applied value = 1 WHERE = '%s' """ % workplace)

        try:
            connection = self.create_connection()
            connection.cursor().execute(injection)
        except Exception as e:
            Exception('Could not update the applying to the workplace, please check error log', e)

    # Saves the workplace to the database
    def save_workplace(self, workplace, worktitle):

        parameters = (workplace, worktitle, 1)

        injection = """INSERT INTO data (workplace, worktitle, applied) VALUES (?,?,?,?);"""

        try:
            connection = self.create_connection()
            connection.cursor().execute(injection,parameters)

        except Exception as e:
            Exception('Could not save workplace, please check error log', e)
