from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""

    Creates a seleniumObject that contains necessary information that is frequently used.
    
"""


class SeleniumObject:

    def __init__(self, url, role, destination):
        self.driver = webdriver.Chrome()
        self.website = self.driver.get(url)
        self.role = role
        self.destination = destination

