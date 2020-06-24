import sqlite3
import Settings.settings as config
from os import path
import os

"""

Handles the Database File

"""


class DB:

    def __init__(self):
        self.file_name = config.settings_dictionary.get('database_name')
        self.pathway = config.settings_dictionary.get('database_path')

    # Checks if the database file exist
    def check_if_file_exist(self):

        # Nested Function
        def creating_database_file():

            try:
                open(self.pathway + self.file_name + '.db', 'w+')
                return 1

            except FileExistsError:
                FileExistsError(" File: " + self.file_name + " couldn't be created, cause already exist!")
                return 0

        # Nested Function
        def creating_directory_path():

            try:

                os.mkdir(self.pathway)
                creating_database_file()
                return 1
            except NotADirectoryError:
                NotADirectoryError('The Directory: ' + self.pathway + "couldn't be created..."
                                                                      "Check so the settings.py is correctly setup")
                return 0

        # Main Function
        if path.isdir(self.pathway):

            if not path.exists(self.pathway + self.file_name):  # Creates file if does not exist.

                def creating_database_file():

                    try:
                        open(self.pathway + self.file_name + '.db', 'w+')
                        return 1

                    except FileExistsError:
                        FileExistsError(" File: " + self.file_name + " couldn't be created, cause already exist!")
                        return 0

                return creating_database_file()

            else:
                return 1

        # Creating directory that is given in the settings.py to store the database inside.
        else:
            return creating_directory_path()
