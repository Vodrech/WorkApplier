from Database.ManagerSQLITE import SQL


class AppliedJobs:

    def __init__(self):
        self.sql = SQL()
        self.table_name = 'applied_jobs'
        self.special_search_table = self.__create_applied_jobs_table()

    def __create_applied_jobs_table(self):

        injection = ("""CREATE TABLE IF NOT EXISTS %s(
        'id' integer NOT NULL,
        'occupation' text,
        'company_name' text,
        'contains_keywords' text,
        'publication_date' text,
        'last_publication_date' text,
        'url' text)""" % self.table_name)

        try:
            connection = self.sql.create_connection()
            connection.cursor().execute(injection)
            connection.commit()
            return 1
        except Exception as e:
            raise Exception('could not create %s table!', e) % self.table_name
        finally:
            connection.close()

    def fetch_applied_jobs(self):

        injection = """SELECT occupation, company_name FROM %s""" % self.table_name

        try:
            connection = self.sql.create_connection()
            data = connection.cursor().execute(injection).fetchall()
            return data

        except Exception as e:
            raise Exception('Could not get all data, please check error log', e)
        finally:
            connection.close()

    def add_job_to_list(self, id, occupation, company_name, contains_keywords, publication_date, last_publication_date, url):

        parameters = (id, occupation, company_name, contains_keywords, publication_date, last_publication_date, url)

        injection = ("""INSERT INTO %s(id, occupation, company_name, contains_keywords, publication_date, last_publication_date, url) VALUES(?,?,?,?,?,?,?)""" % self.table_name)

        try:
            connection = self.sql.create_connection()
            connection.cursor().execute(injection, parameters)
            connection.commit()
            return 1

        except Exception as e:
            raise Exception(e)
        finally:
            connection.close()

    def check_existence(self):

        injection = ("""SELECT id FROM %s""" % self.table_name)

        try:
            connection = self.sql.create_connection()
            data = connection.cursor().execute(injection).fetchall()
            return data

        except Exception as e:
            raise Exception('Could not get all data, please check error log', e)
        finally:
            connection.close()