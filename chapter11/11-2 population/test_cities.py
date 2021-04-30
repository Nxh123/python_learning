import unittest
from city_functions import city_function


class CityTestCase(unittest.TestCase):
    def test_city_function(self):
        city_country = city_function('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago,Chile')

    def test_city_country_population(self):
        city_country_population = city_function('santiago',
                                                'chile',
                                                population=5000000)
        self.assertEqual(city_country_population,
                         'Santiago,Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
