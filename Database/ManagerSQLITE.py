import sqlite3 as sql
import Database.ManagerDB as DB

"""

    Handles all the injections to the database
    Uses the ManagerDB to manage the database file
    
"""


class SQL:

    print('SQL Imported')

    def __init__(self):
        self.database = DB.DB()
        self.connection_string = self.database.pathway + '\\' + self.database.file_name + '.db'
        self.table_existence = self.__create_table()
        self.arbetsformedlingen_existence = self.__create_arbetsformedlningen_table()

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

    def __create_arbetsformedlningen_table(self):
        injection = """CREATE TABLE IF NOT EXISTS data_two('id' integer NOT NULL, 'occupation' text, 'company_name' text, 'contains_keywords' text, 'publication_date' text, 'last_publication_date' text, 'url' text)"""

        try:
            connection = self.create_connection()
            connection.cursor().execute(injection)
            return 1
        except Exception as e:
            raise Exception('could not create data_two table, please check error log', e)
        finally:
            connection.close()

    def __create_settings_table(self):
        injection = """CREATE TABLE IF NOT EXISTS settings('id' integer NOT NULL, 'occupation' text, 'company_name' text, 'contains_keywords' text, 'publication_date' text, 'last_publication_date' text, 'url' text)"""

        try:
            connection = self.create_connection()
            connection.cursor().execute(injection)
            return 1
        except Exception as e:
            raise Exception('could not create settings table!', e)
        finally:
            connection.close()

    def fetch_all_arbetsformedlingen(self):
        try:
            connection = self.create_connection()
            data = connection.cursor().execute("""SELECT id FROM data_two""").fetchall()
            return data

        except Exception as e:
            raise Exception('Could not get all from arbetsformedlningen, please check error log', e)
        finally:
            connection.close()

    def save_workplace_arbetsformedlningen(self, id, occupation, company, contains_keywords, publication_date, last_publication_date, url):

        parameters = (id, occupation, company, contains_keywords, publication_date, last_publication_date, url)

        injection = """INSERT INTO data_two 
        (id, occupation, company_name, contains_keywords, publication_date, last_publication_date, url) 
        VALUES (?, ?, ?, ?, ?, ?, ?);"""

        try:
            connection = self.create_connection()
            connection.cursor().execute(injection, parameters)
            connection.commit()

        except Exception as e:
            raise Exception('Could not save workplace, please check error log', e)
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
            raise Exception('Could not update the applying to the workplace, please check error log', e)
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
            raise Exception('Could not save workplace, please check error log', e)
        finally:
            connection.close()

    def select_all(self):

        try:
            connection = self.create_connection()
            data = connection.cursor().execute("""SELECT * FROM data""").fetchall()
            return data

        except Exception as e:
            raise Exception('Could not get all data, please check error log', e)
        finally:
            connection.close()

