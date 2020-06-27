# Modules imports
import requests
from bs4 import BeautifulSoup

# Folder Imports
import Settings.settings as settings

"""

    The indeed class manage the job searching on linkedin.com

"""


class Indeed:

    def __init__(self):
