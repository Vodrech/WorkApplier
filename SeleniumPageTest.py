from lib2to3.pgen2 import driver

from SeleniumObject import SeleniumObject
from selenium.webdriver.common.keys import Keys
import time

import main
ids = main.applyIndeed()

SB = SeleniumObject("https://se.indeed.com/?from=gnav-homepage", "Testare", "Stockholms Län")

WorkRole = SB.driver.find_element_by_id("text-input-what")
Destination = SB.driver.find_element_by_id("text-input-where")

WorkRole.send_keys(SB.role)
Destination.send_keys(SB.destination, Keys.ENTER)

for s in ids:
    time.sleep(1)
    SB.driver.find_element_by_id(s).click()
    time.sleep(3)
    SB.driver.find_element_by_id('apply-button-container').click()
    time.sleep(30)
    SB.driver.find_element_by_link_text('Ansök').click()

time.sleep(2)

get_title = driver.title

SB = SeleniumObject("")

