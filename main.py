from bs4 import BeautifulSoup
import requests


def applyIndeed():

    appliers = []
    jobTitlesActive = {'Testare', 'Utvecklare', 'Testautomatiserare'}

    sourcePage = requests.get("https://se.indeed.com/Testare-jobb-i-Stockholms-L%C3%A4n").text
    sourceCode = BeautifulSoup(sourcePage, 'lxml')

    for jobs in sourceCode.find_all('div', 'jobsearch-SerpJobCard unifiedRow row result'):

        for elements in jobs.contents:
            for jobtitle in jobTitlesActive:
                if hasattr(elements, 'text'):
                    if str(elements.text).__contains__(jobtitle):
                        jobID = jobs.attrs.get('id')  # Gets the job id so it can parse it to selenium
                        appliers.append(jobID)

    return appliers


if __name__ == '__main__':
    print(applyIndeed())
