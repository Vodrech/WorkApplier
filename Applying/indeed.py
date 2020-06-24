# Modules imports
import requests
from bs4 import BeautifulSoup

# Folder Imports
import Settings.settings as settings

"""

    The indeed class manage the job searching on indeed.com

"""


class Indeed:

    def __init__(self):
        self.job_title = settings.settings_dictionary.get('job_title')
        self.applies = self.__get_workplace_webpage()

    # Method one
    def __get_active_jobs(self):

        """
            Fetches data from a Web page and returns the id on the <div> elements that is being searched after.
            :return: <div> ids
        """

        appliers = []
        source_page = requests.get('https://se.indeed.com/Testare-jobb-i-Stockholms-L%C3%A4n').text #TODO: Fix so it isn't hardcoded, it should adapt after the job_tilte that is given in the settings.py
        source_code = BeautifulSoup(source_page, 'lxml')

        # Fetches the html elements <div>
        for jobs in source_code.find_all('div', 'jobsearch-SerpJobCard unifiedRow row result'):

            for elements in jobs.contents:

                for jobTitle in self.job_title:
                    if hasattr(elements, 'text'):
                        if str(elements.text).__contains__(jobTitle):

                            job_id = jobs.attrs.get('id')  # Gets the job id so it can parse it to get_applies
                            appliers.append(job_id)

        print('Method:', self.__get_active_jobs.__name__, '\nreturned a list of : ', len(appliers))
        return appliers

    # Method two
    def __get_applies(self):

        """
            Uses the first method: get_active_jobs and fetches the elements through their ID's
            :return: Indeeds apply page so workplaces pages can be fetched.
        """

        source_page = requests.get('https://se.indeed.com/Testare-jobb-i-Stockholms-L%C3%A4n').text #TODO: Fix so it isn't hardcoded, it should adapt after the job_tilte that is given in the settings.py
        source_code = BeautifulSoup(source_page, 'lxml')

        job_list = self.__get_active_jobs()
        job_links = []

        # Loops through each job and gets the apply page.
        for job in job_list:

            for selectData in source_code.find_all('div', {'id': job}):  # Finds each div with id element equal to 'job'
                if hasattr(selectData, 'contents'):

                    for s in selectData.contents:
                        if hasattr(s, 'attrs'):

                            attributes = dict(s.attrs)
                            if 'class' in attributes.keys():
                                if 'title' in attributes.get('class'):

                                    for a in s.contents:
                                        if hasattr(a, 'attrs'):

                                            attributes2 = dict(a.attrs)
                                            if 'href' in attributes2.keys():

                                                link = "https://se.indeed.com" + attributes2.get('href')
                                                job_links.append(link)

        print('Method:', self.__get_applies.__name__, '\nfetched:', len(job_links), '/', len(job_list))

        return job_links

    # Method three
    def __get_workplace_webpage(self):

        """
            Uses the Method two: get_applies to fetch the indeed page to able to get the workplace web page
            :return: A list of web pages that is the the workplaces
        """

        links = self.__get_applies()
        workplace_webpages = []

        for link in links:
            source_page = requests.get(link).text
            source_code = BeautifulSoup(source_page, 'lxml')

            for webpage in source_code.find_all('div', 'icl-u-lg-hide'):
                if hasattr(webpage, 'attrs'):

                    attributes = dict(webpage.attrs)
                    if 'class' in attributes.keys():

                        if attributes.get('class').__len__() == 1:
                            if hasattr(webpage, 'contents'):

                                for content in webpage.contents:
                                    if hasattr(content, 'attrs'):

                                        attributes2 = dict(content.attrs)
                                        if 'href' in attributes2.keys():
                                                link = attributes2.get('href')
                                                information = {
                                                    'workplace': source_code.find_all('div', 'icl-u-lg-mr--sm icl-u-xs-mr--xs')[0].text,
                                                    'worktitle': str(source_code.find_all('h3', 'icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title')[0].contents[0]),
                                                    'link': link
                                                }
                                                workplace_webpages.append(information)

        return workplace_webpages
