from bs4 import BeautifulSoup
import requests

dictionary = {
    'sourcePage': 'https://se.indeed.com/Testare-jobb-i-Stockholms-L%C3%A4n'
}

sourcePage = requests.get(dictionary.get('sourcePage')).text
sourceCode = BeautifulSoup(sourcePage, 'lxml')


def get_active_jobs():  # Methods that searches through the job results on indeed.com and verifies it contains the job roles that is selected.

    appliers = []
    jobTitles = {"Testare", "Utvecklare", "TestAutomatiserare"}
    for jobs in sourceCode.find_all('div', 'jobsearch-SerpJobCard unifiedRow row result'):

        for elements in jobs.contents:
            for jobTitle in jobTitles:
                if hasattr(elements, 'text'):
                    if str(elements.text).__contains__(jobTitle):
                        jobID = jobs.attrs.get('id')  # Gets the job id so it can parse it to get_applies
                        appliers.append(jobID)

    print('Method:', get_active_jobs.__name__, '\nreturned a list of : ', len(appliers))
    return appliers


def get_applies():  # Method that finds the link to the jobs.

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


def get_workplace_webpage():  # Gets the work recruiter web-page.

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


def remove_cookie(webpage_URL):

    cookie_dictionary = {
        "cookie"
    }

    sourcePage2 = requests.get(webpage_URL).text
    sourceCode2 = BeautifulSoup(sourcePage2, 'lxml')

    sourceCode2.find_all('div', {'class': cookie_dictionary.pop()})


remove_cookie('https://jobs.academicwork.se/annons/javautvecklare-till-seb-i-stockholm/15042389?utm_source=Indeed&utm_medium=cpc&utm_campaign=Indeed')