import unittest
from Settings.settings import settings_search_dictionary
from Applying.arbetsformedlingen import Arbetsformedlingen


class TestApplying(unittest.TestCase):

    def test_Arbetsformedlingen_instance(self):
        a = Arbetsformedlingen()
        self.assertIsInstance(a, Arbetsformedlingen)

    def test_get_taxonomy_object(self):

        a = Arbetsformedlingen()
        taxList = a._Arbetsformedlingen__get_taxonomy_object()

        if settings_search_dictionary.get('ssyk_active'):
            self.assertEqual(len(settings_search_dictionary.get('ssyk_value')), len(taxList))
        else:
            self.assertEqual(0, len(taxList))

    def test_generate_specific_search(self):

        a = Arbetsformedlingen()

        url = a._Arbetsformedlingen__generate_specific_search()
        self.assertEqual(type(url), str)
        if settings_search_dictionary.get('ssyk_active'):
            for x in a._Arbetsformedlingen__get_taxonomy_object():
                self.assertEqual(True, (url.__contains__('occupation-group=' + str(x))))

        if settings_search_dictionary.get('radius_active'):

            posList = settings_search_dictionary.get('radius_home').split(',')
            lat = posList[0]
            long = posList[1]

            self.assertEqual(True, url.__contains__(('&position=' + lat + '%2C' + long)))

        if settings_search_dictionary.get('limit_active'):

            self.assertEquals(True, url.__contains__(('&limit=' + str(settings_search_dictionary.get('limit_value')))))

    def test_get_active_jobs(self):

        a = Arbetsformedlingen()

        jobs = a.get_active_jobs()

        if settings_search_dictionary.get('limit_active'):
            self.assertEqual(settings_search_dictionary.get('limit_value'), len(jobs))
        else:
            self.assertEquals(10, len(jobs))




