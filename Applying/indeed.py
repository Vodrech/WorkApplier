# Modules imports
import requests
from bs4 import BeautifulSoup


# Folder Imports
import Settings.settings as settings

"""

    The indeed class manage the job searching on indeed.com

"""


@DeprecationWarning
class Indeed:

    def __init__(self):
        self.job_title_filter = settings.settings_dictionary.get('job_title_filter')
        self.search_title = settings.settings_dictionary.get('indeed_search_title')
        self.search_location = settings.settings_dictionary.get('indeed_search_location')
        self.search_published = settings.settings_dictionary.get('indeed_search_published')
        self.applies = self.__get_workplace_webpage()

    # Method one
    def __get_active_jobs(self):

        """
            @Method
            > Fetches data from a Web page and returns the id on the <div> elements that is being searched after.
            > :return: indeed apply page for each job

            @DataFlow
            > Fetch <div> with class = 'jobsearch....'
            > Looks After the H2 Element within the <div> tag
            > Looks for an element with the attributes 'title' and 'href'
            > Saves the href to a list
            > Returns a LIST

        """

        appliers = []
        URL = 'https://se.indeed.com/jobb?q=_&l='.replace('_', self.search_title).__add__(self.search_location).__add__('&fromage=').__add__(self.search_published)
        source_page = requests.get(URL).text  # https://se.indeed.com/Testare-jobb-i-Stockholms-L%C3%A4n
        source_code = BeautifulSoup(source_page, 'lxml')

        # Fetches the html elements <div>
        for jobs in source_code.find_all('div', 'jobsearch-SerpJobCard unifiedRow row result'):

            # Loops through each element within the <div>
            for elements in jobs.contents:

                    if hasattr(elements, 'name'):
                        if elements.name == 'h2':
                            if hasattr(elements, 'contents'):

                                # Loops through the <h2> element and looks for <a> tag
                                for elements2 in elements.contents:
                                    if hasattr(elements2, 'attrs'):

                                                # Checks so its the correct element <a> with the attributes 'href' & 'title'
                                                if elements2.attrs.__contains__('title') and elements2.attrs.__contains__('href'):

                                                    # Checks if the title contains the search terms given in the settings.py
                                                    for jobTitle in self.job_title_filter:
                                                        if elements2.attrs.get('title').casefold().__contains__(jobTitle.casefold()):

                                                            job_link = 'https://se.indeed.com' + elements2.attrs.get('href')
                                                            appliers.append(job_link)

        print('\nMethod:', self.__get_active_jobs.__name__, '\nreturned a list of : ', len(appliers))
        return appliers

    def __get_workplace_webpage(self):

        """
            @Method
            > Uses the __get_active_jobs() to fetch the job applying pages
            :return: A list of job applying pages (URLS)

            @DataFlow
            > Fetches the URL's from __get_active_jobs()
            > Fetches the site and looks for the <div> with class='icl-u-...'
            > Looks after element with the correct attributes
            > Saves a number of dicts to a list
            > Returns a LIST
        """

        links = self.__get_active_jobs()
        workplace_webpages = []

        for link in links:
            source_page = requests.get(link).text
            source_code = BeautifulSoup(source_page, 'lxml')

            for webpage in source_code.find_all('div', 'icl-u-lg-hide'):
                if hasattr(webpage, 'string'):
                    if str(webpage.string).__contains__('Ansök på nästa hemsida'):

                        if hasattr(webpage, 'contents'):
                            for content in webpage.contents:

                                if hasattr(content, 'attrs'):
                                    if content.attrs.__contains__('href'):
                                        web_link = content.attrs.get('href')

                                        information = {
                                            'workplace': source_code.find_all('div', 'icl-u-lg-mr--sm icl-u-xs-mr--xs')[0].text,
                                            'worktitle': str(source_code.find_all('h3','icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title')[0].contents[0]),
                                            'link': web_link
                                        }
                                        workplace_webpages.append(information)

                    else:
                        if hasattr(webpage, 'string'):
                            if str(webpage.string).__contains__('Ansök'):

                                web_link = link
                                information = {
                                    'workplace': source_code.find_all('div', 'icl-u-lg-mr--sm icl-u-xs-mr--xs')[0].text,
                                    'worktitle': str(source_code.find_all('h3','icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title')[0].contents[0]),
                                    'link': web_link
                                }
                                workplace_webpages.append(information)

        print('\nMethod:', self.__get_active_jobs.__name__, '\n found:', len(workplace_webpages), '/', len(links))

        return workplace_webpages
