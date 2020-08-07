import unittest
import os
from Settings.SpecialSearchSettings import settings_search_dictionary
from Settings.SpecialSearchSettings import settings_dictionary
from Settings.save import SaveSettings


class TestApplying(unittest.TestCase):

    def test_ssyk_value(self):

        if settings_search_dictionary.get('ssyk_active'):
            self.assertEqual(type(settings_search_dictionary.get('ssyk_value')), list)

            for x in settings_search_dictionary.get('ssyk_value'):
                self.assertEqual(type(x), int)
        else:
            self.skipTest('The ssyk_active setting were disabled')

    def test_driving_license(self):

        if settings_search_dictionary.get('driving_license_active'):
            self.assertEqual(type(settings_search_dictionary.get('driving_license_value')), str)
        else:
            self.skipTest('The driving_license setting were disabled')

    def test_reduce_working_hours(self):

        if settings_search_dictionary.get('reduce_working_hours_active'):
            self.assertEqual(type(settings_search_dictionary.get('reduce_working_hours_value')), int)
        else:
            self.skipTest('The reduce_working_hours setting were disabled')

    def test_specific_language(self):

        if settings_search_dictionary.get('language_active'):
            self.assertEqual(type(settings_search_dictionary.get('language_value')), str)
        else:
            self.skipTest('The language setting were disabled')

    def test_radius(self):

        if settings_search_dictionary.get('radius_active'):
            self.assertEqual(type(settings_search_dictionary.get('radius_home')), str)
            self.assertEqual(True, settings_search_dictionary.get('radius_home').__contains__(','))
            self.assertEqual(len(settings_search_dictionary.get('radius_home').split(',')), 2)

            self.assertEqual(type(settings_search_dictionary.get('radius_acceptable')), int)
        else:
            self.skipTest('The radius setting were disabled')

    def test_saveSettings_instance(self):
        s = SaveSettings()
        self.assertIsInstance(s, SaveSettings)

    def test_read_settings_file(self):
        s = SaveSettings()
        self.assertEqual(os.path.exists(s.settingsPath))

    def test_save_settings_file(self):
        s = SaveSettings('keywords_value', [])
        s.save_settings_file()




