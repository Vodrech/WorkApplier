import Settings.settings as settings
import json as json
import time
import requests
import logging

# TODO: Sometimes the API dosn't return a JobID Cause UnAuthorized, fix or solve if it isn't solved in the future


"""

    The Arbetsformlingen class manages all the main functionality for searching jobs at arbetsformedlningen.se

"""


class Arbetsformedlingen:

    def __init__(self):
        self.base_url = 'https://jobsearch.api.jobtechdev.se/search?'
        self.base_taxonomy_url = 'https://taxonomy.api.jobtechdev.se/v1/taxonomy/specific/concepts/ssyk?'
        self.logger = logging.getLogger('applying')

    def __get_taxonomy_object(self):

        """

            @Method
            > Fetching Taxonomy object from the arbetsformedling API.
            > :return: A list of ID's on the occuppation roles.

            @DataFlow
            > Uses the SSYK standard to fetch the ID for an specific occuppation role.
            > Adds the ID to a list
            > :return: A list with ID's

        """

        url = self.base_taxonomy_url + 'ssyk-code-2012='    # Hardcoded cause only one object is needed, if more object is needed, make a more adaptive url
        headers = {'api-key': settings.settings_dictionary.get('api_key')}
        occupation_roles = []
        unAuthorizedCounter = 0

        if settings.settings_search_dictionary.get('ssyk_active') is True:

            for value in settings.settings_search_dictionary.get('ssyk_value'):

                while unAuthorizedCounter < 10:     # Tries 10 times to authorize

                    source_page = requests.get(url + str(value), headers=headers)
                    unAuthorizedCounter+=1  # Fix (Before ++) Now ( += )
                    time.sleep(1)                       # TODO: Takes to long time with sleep, fix

                    if source_page.status_code is 200:  # TODO: Fix Exception Handling for status codes such as 401 or 501

                        id = json.loads(source_page.text)[0].get('taxonomy/id')
                        occupation_roles.append(id)
                        break

        self.logger.info('Occupation_roles found:' + str(occupation_roles))

        return occupation_roles

    def __generate_specific_search(self):

        """

            @Method
            > Generates a URL so the request library can use the API to fetch requested elements.
            > :return: A URL with all requested elements within it.

            @DataFlow
            > Takes in the a list from the get_taxonomy_object
            > Adds all the elements that is wanted to the specific search to an URL
            > :return: A URL string to fetch data from the API.

        """

        url = self.base_url

        # Occupation is enabled in settings.py
        if settings.settings_search_dictionary.get('ssyk_active') is True:
            occupation_list = self.__get_taxonomy_object()

            if len(occupation_list) > 0:

                for occupation_index, occupation_value in enumerate(occupation_list):

                    url = url + 'occupation-group=' + occupation_value

                    if (occupation_index + 1) != len(occupation_list):
                        url = url + '&'

            else:
                raise Exception('The "ssyk_active" were "True" but no occupation were given')

        # Driving licence is enabled in settings.py
        if settings.settings_search_dictionary.get('driving_license_active'):
            print('WOW')    # FIX

        # Specific position of workplace is enabled in settings.py
        if settings.settings_search_dictionary.get('radius_active'):
            homePos = settings.settings_search_dictionary.get('radius_home').split(',')

            if len(homePos) <= 2:

                homeLat = homePos[0]
                homeLong = homePos[1]
                url = url + '&' + 'position=' + homeLat + '%2C' + homeLong


            else:
                raise Exception('The "radius_active" were "True" but value were entered wrong. Example(59.434,18.242)')

        if settings.settings_search_dictionary.get('limit_active'):
            if int(settings.settings_search_dictionary.get('limit_value')) > 100:
                raise Exception('The limit can only be 100 or less')
            elif type(settings.settings_search_dictionary.get('limit_value')) == float:
                raise Exception('The limit can only be an integer, eg ( 1, 50, 100) not (1.0, 50.5, 100.58)')
            else:
                url = url + '&limit=' + str(settings.settings_search_dictionary.get('limit_value'))

        return url

    def get_active_jobs(self):

        """

            @Method
            > Fetches all the jobs after the configurations have been made
            > :return: A list with a bunch of jobs

            @DataFlow
            >
            > Adds all the elements that is wanted to the specific search to an URL
            > :return: A URL string to fetch data from the API.

        """

        url = self.__generate_specific_search()

        if settings.settings_dictionary.get('api_key').strip(' ') == '':
            raise Exception('The api-key is missing in the settings.py file')

        headers = {'api-key': settings.settings_dictionary.get('api_key')}

        source_page = requests.get(url, headers=headers)

        if source_page.status_code == 200:

            source_page.encoding = settings.settings_dictionary.get('encoding')
            results = json.loads(source_page.text).get('hits')

            if len(results) == 0:
                raise Exception('No Matches where found, please check so that the url were correct!')

            return results

        elif source_page.status_code is 401:
            raise Exception('Unauthorized, Please check so that your API key is valid!')

        elif source_page.status_code is 501:
            raise Exception('The server for the API is currently unavailable, please check back later!')
