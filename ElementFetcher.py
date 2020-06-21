from SeleniumObject import SeleniumObject
from selenium.webdriver.common.keys import Keys
import main
import time


class ElementFetcher:


    def test(self):
        SB = SeleniumObject("https://se.indeed.com/?from=gnav-homepage", "Testare", "Stockholms Län")

        WorkRole = SB.driver.find_element_by_id("text-input-what")
        Destination = SB.driver.find_element_by_id("text-input-where")

        WorkRole.send_keys(SB.role)
        Destination.send_keys(SB.destination, Keys.ENTER)

        JobCard = SB.driver.find_element_by_css_selector("div[class='jobsearch-SerpJobCard unifiedRow row result clickcard']")


        time.sleep(2)

    listYEE = main.get_workplace_webpage()
    SeleniumObject(listYEE[0], "Testare", "Stockholms Län")
    time.sleep(2)


