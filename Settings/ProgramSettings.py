import os
import sys


class ProgramConfigurations:

    val = '\\DB' if sys.platform[0] == 'w' else '/DB'

    program_settings = {

        'main_folder': (os.getcwd().split('WorkApplier')[0] + 'WorkApplier'),
        'db_folder': val,                    # Database Folder
        'database_name': 'WorkApplier DB',  # Database Name
        'encoding': 'utf8',                     # Encoding for the return value after work available result
        'api_key': 'YidceGY4XHhlMFx4ZjQiL2lceGI5XHhmYVx4ZTB7XHhjY1x4ZmFCXS5ceGIxXHhhM2ZWeCc',

        # Deprecated Settings
        'job_title_filter': ('',),  # Tuple , special search after title
        'indeed_search_title': '',  # String
        'indeed_search_location': '',  # String
        'indeed_search_published': ''  # String , Given in days choose between ( 1, 3 , 7 , 14 )

    }
