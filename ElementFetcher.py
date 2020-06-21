from SeleniumObject import SeleniumObject
from selenium.webdriver.common.keys import Keys
import main
import time
import Database.ManagerDB as db


class ElementFetcher:


    def test(self):
        SB = SeleniumObject("https://se.indeed.com/?from=gnav-homepage", "Testare", "Stockholms Län")

        WorkRole = SB.driver.find_element_by_id("text-input-what")
        Destination = SB.driver.find_element_by_id("text-input-where")

        WorkRole.send_keys(SB.role)
        Destination.send_keys(SB.destination, Keys.ENTER)

        JobCard = SB.driver.find_element_by_css_selector("div[class='jobsearch-SerpJobCard unifiedRow row result clickcard']")


        time.sleep(2)


    DB_Object = db.DB()
    DB_Object.check_if_file_exist()





