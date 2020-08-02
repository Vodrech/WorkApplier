import logging

"""

The Settings File is the settings for the program to function correctly.
Please edit this file if something is wanted, the basic configuration should...
work correctly anyways.

Prerequisites:
    If the folder is protected by admin rights, please create a folder by yourself and link it through the database_path


"""

# Settings for program functionality
settings_dictionary = {

    'main_folder': 'C:\Temp',
    'db_folder': '\\DB',                    # Database Folder
    'api_folder': '\\API',                  # API Folder
    'database_name': 'WorkApplier DB',  # Database Name
    'encoding': 'utf8',                     # Encoding for the return value after work available result
    'api_key': '',

    # Deprecated Settings
    'job_title_filter': ('',),  # Tuple , special search after title
    'indeed_search_title': '',  # String
    'indeed_search_location': '',  # String
    'indeed_search_published': ''  # String , Given in days choose between ( 1, 3 , 7 , 14 )

}

# Special search settings
settings_search_dictionary = {

    # Occupations, entered as a list (SSYK)
    'ssyk_active': False,
    'ssyk_value': [],

    # Driving license
    'driving_license_active': False,
    'driving_license_value': '',
    'driving_license_own_car': False,
    # ADD ? Driving license required for that occupation

    # Reduce working hours, default = 100
    'reduce_working_hours_active': False,
    'reduce_working_hours_value': '',

    # Specific Language needed
    'language_active': False,
    'language_required': True,
    'language_value': '',

    # Specific position range from home to work, (latitude,longitude)
    'radius_active': False,
    'radius_home': '',
    'radius_acceptable': '',

    # Description keywords searcher , If specific keywords in the job description
    'keywords_active': False,
    'keywords_value': [],

    # Number of jobs that the function is going to fetch, standard 10
    'limit_active': False,
    'limit_value': '',

}
