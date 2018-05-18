import unittest

import pandas as pd

DATA_PATH = 'data'
TEST_DATA_PATH = 'data/test'

class DataFileTests(unittest.TestCase):
    def test_a_test_file_exists(self):
        df = pd.read_csv(f'{TEST_DATA_PATH}/Shot2017.TXT')
        self.assertEqual(999, len(df))

    def test_a_non_test_file_exists(self):
        df = pd.read_csv(f'{DATA_PATH}/CourseLevel2013.TXT')
        self.assertEqual(2772, len(df))
