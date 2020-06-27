import logging

"""

The Settings File is the settings for the program to function correctly.
Please edit this file if something is wanted, the basic configuration should...
work correctly anyways.

Prerequisites:
    If the folder is protected by admin rights, please create a folder by yourself and link it through the database_path


"""


settings_dictionary = {
    'database_name': 'WorkPlaces Applied',  # String
    'database_path': 'C:\\Temp\\',          # Fails when creating directory cause it should only be named C:\\Temp
    'job_title_filter': ('',),       # Tuple , special search after title
    'indeed_search_title': 'Testare',       # String
    'indeed_search_location': 'Stockholm',  # String
    'indeed_search_published': '14'         # String , Given in days choose between ( 1, 3 , 7 , 14 )
}