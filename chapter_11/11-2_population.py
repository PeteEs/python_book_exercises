import unittest
from population import city_country_population

class NameTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_address = city_country_population("santiago","chile")
        self.assertEqual(formatted_address,"Santiago, Chile")

    def test_city_country_population(self):
        formatted_address = city_country_population("santiago","chile",5000000)
        self.assertEqual(formatted_address,"Santiago, Chile - population 5000000")

if __name__ == '__main__':
    unittest.main()
