from Database.Tables.TableSpecialSearch import SpecialSearch

"""

The Settings File is the settings for the program to function correctly.
Please edit this file if something is wanted, the basic configuration should...
work correctly anyways.

Prerequisites:
    If the folder is protected by admin rights, please create a folder by yourself and link it through the database_path


"""


class Settings:

    def __init__(self):
        self.special_search = SpecialSearch()
        self.special_settings = self.special_search.fetch_settings()

# Settings for program functionality

    def get_special_search_settings(self, object):

        special_search_settings = {

            # Occupations, entered as a list (SSYK)
            'ssyk_active': self.special_settings[0],
            'ssyk_value': self.special_settings[1],

            # Driving license
            'driving_license_active': self.special_settings[2],
            'driving_license_value': self.special_settings[3],
            'driving_license_own_car': self.special_settings[4],
            # ADD ? Driving license required for that occupation

            # Reduce working hours, default = 100
            'reduce_working_hours_active': self.special_settings[5],
            'reduce_working_hours_value': self.special_settings[6],

            # Specific Language needed
            'language_active': self.special_settings[7],
            'language_required': self.special_settings[8],
            'language_value': self.special_settings[9],

            # Specific position range from home to work, (latitude,longitude)
            'radius_active': self.special_settings[10],
            'radius_home_lat': self.special_settings[11],
            'radius_home_long': self.special_settings[12],
            'radius_acceptable': self.special_settings[13],

            # Description keywords searcher , If specific keywords in the job description
            'keywords_active': self.special_settings[14],
            'keywords_value': self.special_settings[15],

            # Number of jobs that the function is going to fetch, standard 10
            'limit_active': self.special_settings[16],
            'limit_value': self.special_settings[17],

        }

        value = special_search_settings.get(object)
        return value
