from Settings.ProgramSettings import ProgramConfigurations
from Settings.SpecialSearchSettings import Settings
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
        self.dataConfigurations = Settings()

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
        headers = {'api-key': ProgramConfigurations.program_settings.get('api_key')}
        occupation_roles = []
        unAuthorizedCounter = 0

        if self.dataConfigurations.get_special_search_settings('ssyk_active') == 1:

            for value in self.dataConfigurations.get_special_search_settings('ssyk_value').split(' '):

                while unAuthorizedCounter < 10:     # Tries 10 times to authorize

                    source_page = requests.get(url + str(value), headers=headers)
                    unAuthorizedCounter+=1
                    time.sleep(0.1)
                    status_code = source_page.status_code
                    if source_page.status_code is 200:

                        id = json.loads(source_page.text)[0].get('taxonomy/id')
                        occupation_roles.append(id)
                        break

                    if status_code is 401:
                        raise Exception('Could not fetch taxonomy_object cause status_code were 401 (unauthorized)')
                    elif status_code is 501:
                        raise Exception('Could not fetch taxonomy_object cause status_code were 501 (Server Issue)')

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

        # Occupation is enabled in TableSpecialSearch.py
        if self.dataConfigurations.get_special_search_settings('ssyk_active'):
            occupation_list = self.__get_taxonomy_object()

            if len(occupation_list) > 0:

                for occupation_index, occupation_value in enumerate(occupation_list):

                    url = url + 'occupation-group=' + occupation_value

                    if (occupation_index + 1) != len(occupation_list):
                        url = url + '&'

            else:
                raise Exception('The "ssyk_active" were "True" but no occupation were given')

        if self.dataConfigurations.get_special_search_settings('reduce_working_hours_active'):
            percentage = self.dataConfigurations.get_special_search_settings('reduce_working_hours_value')
            url = url + '&' + 'parttime.max=' + str(percentage)

        # Driving licence is enabled in TableSpecialSearch.py
        if self.dataConfigurations.get_special_search_settings('driving_license_active'):
            # B = VTK8_WRx_GcM

            url = url + '&' + 'driving-license-required=true'

        # Specific position of workplace is enabled in TableSpecialSearch.py
        if self.dataConfigurations.get_special_search_settings('radius_active'):

            homeLat = self.dataConfigurations.get_special_search_settings('radius_home_lat')
            homeLong = self.dataConfigurations.get_special_search_settings('radius_home_long')

            url = url + '&' + 'position=' + str(homeLat) + '%2C' + str(homeLong)

        if self.dataConfigurations.get_special_search_settings('limit_active'):
            if int(self.dataConfigurations.get_special_search_settings('limit_value')) > 100:
                raise Exception('The limit can only be 100 or less')
            elif type(self.dataConfigurations.get_special_search_settings('limit_value')) == float:
                raise Exception('The limit can only be an integer, eg ( 1, 50, 100) not (1.0, 50.5, 100.58)')
            else:
                url = url + '&limit=' + str(self.dataConfigurations.get_special_search_settings('limit_value'))

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

        if ProgramConfigurations.program_settings.get('api_key').strip(' ') == '':
            raise Exception('The api-key is missing in the TableSpecialSearch.py file')

        headers = {'api-key': ProgramConfigurations.program_settings.get('api_key')}

        source_page = requests.get(url, headers=headers)

        if source_page.status_code == 200:

            source_page.encoding = self.dataConfigurations.get_special_search_settings('encoding')
            results = json.loads(source_page.text).get('hits')

            if len(results) == 0:
                raise Exception('No Matches where found, problems: search criteria to specific? Or development bug?')

            return results

        elif source_page.status_code is 401:
            raise Exception('Unauthorized, Please check so that your API key is valid!')

        elif source_page.status_code is 501:
            raise Exception('The server for the API is currently unavailable, please check back later!')
