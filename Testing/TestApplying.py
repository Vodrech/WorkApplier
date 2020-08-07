import unittest
from Settings.SpecialSearchSettings import Settings
from Applying.arbetsformedlingen import Arbetsformedlingen


class TestApplying(unittest.TestCase):

    def test_Arbetsformedlingen_instance(self):
        a = Arbetsformedlingen()
        self.assertIsInstance(a, Arbetsformedlingen)

    def test_get_taxonomy_object(self):
        s = Settings()

        a = Arbetsformedlingen()
        taxList = a._Arbetsformedlingen__get_taxonomy_object()

        if s.get_special_search_settings('ssyk_active'):
            self.assertEqual(len(s.get_special_search_settings('ssyk_value')), len(taxList))
        else:
            self.assertEqual(0, len(taxList))

    def test_generate_specific_search(self):

        s = Settings()

        a = Arbetsformedlingen()

        url = a._Arbetsformedlingen__generate_specific_search()
        self.assertEqual(type(url), str)
        if s.get_special_search_settings('ssyk_active'):
            for x in a._Arbetsformedlingen__get_taxonomy_object():
                self.assertEqual(True, (url.__contains__('occupation-group=' + str(x))))

        if s.get_special_search_settings('radius_active'):

            posList = s.get_special_search_settings('radius_home').split(',')
            lat = s.get_special_search_settings('radius_home_lat')
            long = s.get_special_search_settings('radius_home_long')

            self.assertEqual(True, url.__contains__(('&position=' + lat + '%2C' + long)))

        if s.get_special_search_settings('limit_active'):

            self.assertEquals(True, url.__contains__(('&limit=' + str(s.get_special_search_settings('limit_value')))))

    def test_get_active_jobs(self):
        s = Settings()

        a = Arbetsformedlingen()

        jobs = a.get_active_jobs()

        if s.get_special_search_settings('limit_active'):
            self.assertEqual(s.get_special_search_settings('limit_value'), len(jobs))
        else:
            self.assertEquals(10, len(jobs))




