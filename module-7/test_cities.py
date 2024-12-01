# Megan Wheeler
# Assignment 7.2
# 30 November 2024

import unittest
from city_functions import get_city_country

class CitiesTestCase(unittest.TestCase):

    # Tests for 'city_functions.py'.

    def test_city_country(self):

        # Do names like 'Dublin, Ireland' work?

        formatted_city_name = get_city_country('dublin', 'ireland')

        self.assertEqual(formatted_city_name, 'Dublin, Ireland')

if __name__ == '__main__':
    unittest.main()