import unittest
from city_functions import city_function


class CityTestCase(unittest.TestCase):
    def test_city_function(self):
        city_country = city_function('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago,Chile')


if __name__ == '__main__':
    unittest.main()
