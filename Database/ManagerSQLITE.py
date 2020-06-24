import sqlite3 as sql
import Database.ManagerDB as DB

"""

    Handles all the injections to the database
    Uses the ManagerDB to manage the database file
    
"""


class SQL:

    def __init__(self):
        self.database = DB.DB()
        self.connection_string = self.database.pathway + self.database.file_name + '.db'
        self.table_existence = self.__create_table()

    def create_connection(self):

        try:
            conn = sql.connect(self.connection_string)
            return conn

        except ConnectionError as e:
            ConnectionError('Connection between sqlite could not be established, please see error', e)

    def __create_table(self):

        injection = """CREATE TABLE IF NOT EXISTS data
        ('workplace' text NOT NULL, 'worktitle' text, 'link' text, 'applied' integer DEFAULT 0)"""

        try:
            connection = self.create_connection()
            connection.cursor().execute(injection)
            return 1
        except Exception as e:
            Exception('Could not create the database table, please check error log', e)
        finally:
            connection.close()

    # Applies to a workplace
    def apply(self, workplace):

        injection = ("""UPDATE data SET applied value = 1 WHERE = '%s' """ % workplace)

        try:
            connection = self.create_connection()
            connection.cursor().execute(injection)
            connection.commit()

        except Exception as e:
            Exception('Could not update the applying to the workplace, please check error log', e)
        finally:
            connection.close()

    # Saves the workplace to the database
    def save_workplace(self, workplace, worktitle, link):

        parameters = (workplace, worktitle, link)

        injection = """INSERT INTO data (workplace, worktitle, link, applied) VALUES (?, ?, ?, 0);"""

        try:
            connection = self.create_connection()
            connection.cursor().execute(injection, parameters)
            connection.commit()

        except Exception as e:
            Exception('Could not save workplace, please check error log', e)
        finally:
            connection.close()

    def select_all(self):

        try:
            connection = self.create_connection()
            data = connection.cursor().execute("""SELECT * FROM data""").fetchall()
            return data

        except Exception as e:
            Exception('Could not get all data, please check error log', e)
        finally:
            connection.close()

