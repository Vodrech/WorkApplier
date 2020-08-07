from Database.ManagerSQLITE import SQL

"""

    The Settings table in the database

"""


class SpecialSearch:

    def __init__(self):
        self.sql = SQL()
        self.table_name = 'special_search'
        self.special_search_table = self.__create_special_search_table()

    def __create_special_search_table(self):

        injection = ("""CREATE TABLE IF NOT EXISTS %s(
        ssyk_active BOOLEAN NOT NULL CHECK (ssyk_active IN (0,1)), ssyk_value text, 
        driving_license_active BOOLEAN NOT NULL CHECK (driving_license_active IN (0,1)), driving_license_value text, driving_license_own_car BOOLEAN NOT NULL CHECK (driving_license_own_car IN (0,1)),
        reduce_working_hours_active BOOLEAN NOT NULL CHECK (reduce_working_hours_active IN (0,1)), reduce_working_hours_value integer,
        language_active BOOLEAN NOT NULL CHECK (language_active IN (0,1)), language_required BOOLEAN NOT NULL CHECK (language_required IN (0,1)), language_value text,
        radius_active BOOLEAN NOT NULL CHECK (radius_active IN (0,1)), radius_home_lat NUMERIC, radius_home_long NUMERIC, radius_acceptable integer,
        keywords_active BOOLEAN NOT NULL CHECK (keywords_active IN (0,1)), keywords_value text,
        limit_active BOOLEAN NOT NULL CHECK (limit_active IN (0,1)), limit_value integer
        )""" % self.table_name)

        try:
            connection = self.sql.create_connection()
            connection.cursor().execute(injection)
            connection.commit()
            return 1
        except Exception as e:
            raise Exception('could not create settings table!', e)
        finally:
            connection.close()

    def fetch_settings(self):

        injection = (""" SELECT * FROM %s""" % self.table_name)

        try:
            connection = self.sql.create_connection()
            data = connection.cursor().execute(injection).fetchone()
            return data
        except Exception as e:
            raise Exception('could not create settings table!', e)
        finally:
            connection.close()

    def save_settings(self, ssyk_active, ssyk_value, driving_license_active, driving_license_value, driving_license_own_car, reduce_working_hours_active, reduce_working_hours_value,
                      language_active, language_required, language_value, radius_active, radius_home_lat, radius_home_long, radius_acceptable, keywords_active, keywords_value, limit_active, limit_value):

        parameters = (ssyk_active, ssyk_value, driving_license_active, driving_license_value, driving_license_own_car, reduce_working_hours_active, reduce_working_hours_value,
                      language_active, language_required, language_value, radius_active, radius_home_lat, radius_home_long, radius_acceptable, keywords_active, keywords_value, limit_active, limit_value)

        injection = (
                """INSERT INTO %s
                (ssyk_active, ssyk_value,
                driving_license_active, driving_license_value, driving_license_own_car,
                reduce_working_hours_active, reduce_working_hours_value,
                language_active, language_required, language_value,
                radius_active, radius_home_lat, radius_home_long, radius_acceptable,
                keywords_active, keywords_value, limit_active, limit_value) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""" % self.table_name)

        try:
            connection = self.sql.create_connection()
            connection.cursor().execute(injection, parameters)
            connection.commit()
            return 1
        except Exception as e:
            raise Exception('could not create settings table!', e)
        finally:
            connection.close()

    def delete_settings(self):

        injection = ("""DELETE FROM %s;""" % self.table_name)

        try:
            connection = self.sql.create_connection()
            connection.cursor().execute(injection)
            connection.commit()
            return 1
        except Exception as e:
            raise Exception('could not create settings table!', e)
        finally:
            connection.close()


# s = SpecialSearch()
# a = s.save_settings(1,2514,1,'B',1,0,'',0,0,'',1,19.2,18.2,10,1,'java sql python',1,10)
# print(a)
