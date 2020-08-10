from Applying.indeed import Indeed
from Applying.arbetsformedlingen import Arbetsformedlingen
from Database.ManagerSQLITE import SQL
from Settings.SpecialSearchSettings import Settings


"""

    The ApplyingInterface is the entry point for searching jobs on different job searching sites
    The main site is Arbetsformedlning.se but further sites may be added in the further if needed.

"""


class ApplyingInterface:

    print('Workflow Imported')

    def __init__(self):
        self.sql = SQL()    # Creates the SQL object so SQL injections can be made
        self.saved_jobs = self.sql.select_all()
        self.exists = True
        self.dataConfigurations = Settings()

    @DeprecationWarning
    def apply_indeed(self):

        print('saving to database')

        for saveWorkPlace in self.indeed.applies:

            for job in self.saved_jobs:

                if job.__contains__(saveWorkPlace.get('workplace')) and job.__contains__(saveWorkPlace.get('worktitle')):
                    self.exists = False

            if self.exists is True:

                workplace = saveWorkPlace.get('workplace')
                worktitle = saveWorkPlace.get('worktitle')
                link = saveWorkPlace.get('link')
                print('Saving to DB: ', workplace, '-', worktitle)
                self.sql.save_workplace(workplace, worktitle, link)

            else:
                print('\nJob Already exist: ', saveWorkPlace.get('workplace'), '-', saveWorkPlace.get('worktitle'))

    # Applying Arbetsformedlningen Function
    def apply_arbetsformedlningen(self):

        """

            @Method
            > Uses the arbetsformedlingen class to fetch data and save to database.

            @DataFlow
            > Creates new instance of Arbetsformedlingen class
            > Fetches all the data that is generated from that class, eg jobs
            > Fetches the stored data and compares to the newly fetch so no duplicates are being stored
            > Checks the job description if it contains keywords that is given in the TableSpecialSearch.py file
            > Fetches all the data that is necessary
            > Stores the data

        """

        AF = Arbetsformedlingen()

        fetched_data = AF.get_active_jobs()
        saved_data = self.sql.fetch_all_arbetsformedlingen()

        # Nested Function , Checks if the any job saved in the db has the same id
        def check_existence(data):

            if len(saved_data) == 0:
                return 0

            for s in saved_data:

                id = int(data.get('id'))

                if id == s[0]:
                    return 1

            return 0

        # Nested Function, checks if the description contains any of keywords in the TableSpecialSearch.py
        def keywords_description(data):

            keyword_dict = {}
            text = data.get('description').get('text').lower()
            boolVal = self.dataConfigurations.get_special_search_settings('keywords_active')

            if boolVal == True:
                keyword_list = self.dataConfigurations.get_special_search_settings('keywords_value').split(' ')

                for keyword in keyword_list:
                    if text.__contains__(keyword.lower()):
                        keyword_dict[keyword] = True
                    else:
                        keyword_dict[keyword] = False

            return keyword_dict

        # Nested Function , gets all the necessary data to save to database
        def get_all_necessary_data(data):

            data_dict = {}

            # Fetching ID
            if 'id' not in data_dict.keys():
                data_dict['id'] = data.get('id')
            else:
                raise Exception('Dict already has an element named "id"')

            # Fetching occupation
            if 'occupation' not in data_dict.keys():
                data_dict['occupation'] = data.get('occupation').get('label')
            else:
                raise Exception('Dict already has an element named "id"')

            # Fetching company_name
            if 'company' not in data_dict.keys():
                data_dict['company'] = data.get('employer').get('name')
            else:
                raise Exception('Dict already has an element named "company"')

            keyword_dict = keywords_description(data)
            keyword_list = self.dataConfigurations.get_special_search_settings('keywords_value').split(' ')
            keywords_found = ""
            for keyword in keyword_list:

                boolVal2 = keyword_dict.get(keyword)

                if boolVal2 is True:
                    keywords_found = keywords_found + keyword + ', '

            # Fetching keywords
            if 'contains_keyword' not in data_dict.keys():
                data_dict['contains_keyword'] = keywords_found
            else:
                raise Exception('Dict already has an element named "contains_keyword"')

            # Fetching publication_date
            if 'publication_date' not in data_dict.keys():
                data_dict['publication_date'] = data.get('publication_date').split('T')[0]
            else:
                raise Exception('Dict already has an element named "publication_date"')

            # Fetching last_publication_date
            if 'last_publication_date' not in data_dict.keys():
                data_dict['last_publication_date'] = data.get('last_publication_date').split('T')[0]
            else:
                raise Exception('Dict already has an element named "last_publication_date"')

            # Fetching url
            if 'application_details' not in data_dict.keys():
                if 'url' in data.get('application_details').keys():
                     url = data.get('application_details').get('url')
                     if url == None:
                         data_dict['url'] = data.get('webpage_url')
                     else:
                         data_dict['url'] = url
            else:
                raise Exception('Dict already has an element named "publication_date"')

            return data_dict

        def save_all_data(dictionary):

            id = dictionary.get('id')
            occupation = dictionary.get('occupation')
            company = dictionary.get('company')
            contains_keyword = dictionary.get('contains_keyword')
            publication_date = dictionary.get('publication_date')
            last_publication_date = dictionary.get('last_publication_date')
            url = dictionary.get('url')

            self.sql.save_workplace_arbetsformedlningen(id, occupation, company, contains_keyword, publication_date, last_publication_date, url)

        # Main Functionality, Loops through each object in the returned list

        for d2 in fetched_data:
            boolVal = check_existence(d2)

            if boolVal != True:

                save_all_data(get_all_necessary_data(d2))

            else:
                print("Job already exist... skips to add it to the DB")
