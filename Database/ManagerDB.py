from os import path
import os
import sys
"""

Handles the Database File

"""

val = '\\DB' if sys.platform[0] == 'w' else '/DB'
fileSeperator = '\\' if sys.platform[0] == 'w' else '/'


class DB:

    print('Manager DB Imported')

    def __init__(self):
        self.file_name = 'WorkApplier'  # TODO: FIX
        self.pathway = (os.getcwd().split('WorkApplier')[0] + 'WorkApplier' + val)
        self.check_if_file_exist()

    # Checks if the database file exist
    def check_if_file_exist(self):

        # Nested Function
        def creating_database_file():

            try:
                open(self.pathway + fileSeperator + self.file_name + '.db', 'w+')
                return 1

            except FileExistsError:
                raise FileExistsError(" File: " + self.file_name + " couldn't be created, cause already exist!")
                return 0

        # Nested Function
        def creating_directory_path():

            try:

                os.mkdir(self.pathway)
                creating_database_file()
                return 1
            except NotADirectoryError:
                raise NotADirectoryError('The Directory: ' + self.pathway + "couldn't be created..."
                                                                      "Check so the TableSpecialSearch.py is correctly setup")
                return 0

        # Main Function
        if path.isdir(self.pathway):

            if not path.exists(self.pathway + fileSeperator + self.file_name + '.db'):  # Creates file if does not exist.

                def creating_database_file():

                    try:
                        open(self.pathway + self.file_name + '.db', 'w+')
                        return 1

                    except FileExistsError:
                        raise FileExistsError(" File: " + self.file_name + " couldn't be created, cause already exist!")
                        return 0

                return creating_database_file()

            else:
                return 1

        # Creating directory that is given in the TableSpecialSearch.py to store the database inside.
        else:
            return creating_directory_path()
