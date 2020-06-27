import Settings.settings as settings

import requests
from bs4 import BeautifulSoup

class Arbetsformedlingen:

    def __init__(self):
        self.job_title_filter = settings.settings_dictionary.get('job_title_filter')
        self.search_title = settings.settings_dictionary.get('indeed_search_title')
        self.search_location = settings.settings_dictionary.get('indeed_search_location')
        self.search_published = settings.settings_dictionary.get('indeed_search_published')
        self.applies = self.__get_workplace_webpage()


    source_page = requests.get('https://arbetsformedlingen.se/platsbanken/annonser').text
    source_code = BeautifulSoup(source_page, 'lxml')

    for s in source_code.find_all('ul', '_ngcontent-asy-c12'):
        print(5)

