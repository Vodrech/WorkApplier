# Modules imports
import requests
from bs4 import BeautifulSoup

# Folder Imports
import Settings.settings as settings
import Database.ManagerSQLITE as SQL

"""

Does the job searching on indeed.com

"""


class Indeed:

    def __init__(self):
        self.job_title = settings.settings_dictionary.get('job_title')
        self.sql = SQL.SQL()
        self.applies = []

    def get_active_jobs(self):  # Methods that searches through the job results on indeed.com and verifies it contains the job roles that is selected.

        appliers = []
        sourcePage = requests.get('https://se.indeed.com/Testare-jobb-i-Stockholms-L%C3%A4n').text #TODO: Fix so it isn't hardcoded, it should adapt after the job_tilte that is given in the settings.py
        sourceCode = BeautifulSoup(sourcePage, 'lxml')

        for jobs in sourceCode.find_all('div', 'jobsearch-SerpJobCard unifiedRow row result'):

            for elements in jobs.contents:
                for jobTitle in self.job_title:
                    if hasattr(elements, 'text'):
                        if str(elements.text).__contains__(jobTitle):
                            jobID = jobs.attrs.get('id')  # Gets the job id so it can parse it to get_applies
                            appliers.append(jobID)

        print('Method:', get_active_jobs.__name__, '\nreturned a list of : ', len(appliers))
        return appliers

    def get_applies(self):  # Method that finds the link to the jobs.

        jobList = get_active_jobs()
        job_links = []

        for job in jobList:#Loops through each job and gets the apply page.

            for selectData in sourceCode.find_all('div', {'id': job}):  # Finds each div with id element equal to 'job'
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

        print('Method:', get_applies.__name__, '\nfetched:', len(jobList), '/', len(job_links))

        return job_links

    def get_workplace_webpage(self):  # Gets the work recruiter web-page.

        links = get_applies()
        workplace_webpages = []

        for link in links:
            sourcePage2 = requests.get(link).text
            sourceCode2 = BeautifulSoup(sourcePage2, 'lxml')

            for webpage in sourceCode2.find_all('div', 'icl-u-lg-hide'):
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
                                                workplace_webpages.append(link)

        return workplace_webpages
