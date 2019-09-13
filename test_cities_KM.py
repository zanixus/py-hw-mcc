#!/usr/bin/python3
"""
    Kevin M. Mallgrave
    CTIM-285 W01 / Professor Janet Brown-Sederberg
    17 May 2019

    version 1.0: initial release
"""

import unittest
from city_functions_KM import city_country

class CitiesTestCase(unittest.TestCase):

    def test_city_country(self):
        vladivostok_russia = city_country('vladivostok', 'russia')
        self.assertEqual(vladivostok_russia, 'Vladivostok, Russia')
        hell_usa = city_country('new york city', 'united states', 8398748)
        self.assertEqual(hell_usa, 'New York City, United States - population 8398748')

unittest.main()
