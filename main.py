from bs4 import BeautifulSoup
import requests


def apply():

    jobTitlesActive = {'Testare', 'Utvecklare', 'Testautomatiserare'}


    sourcePage = requests.get("https://se.indeed.com/Testare-jobb-i-Stockholms-L%C3%A4n").text
    sourceCode = BeautifulSoup(sourcePage, 'lxml')

    for jobs in sourceCode.find_all('div', 'jobsearch-SerpJobCard unifiedRow row result'):
        content = jobs.text
        for jobtitle in jobTitlesActive:
            str(content).__contains__(jobtitle)



    sourceCode.find_all('div', 'jobsearch-SerpJobCard unifiedRow row result')


if __name__ == '__main__':
    apply()
