import unittest
from city_country import city_country_fun

class NameTestCase(unittest.TestCase):

    def test_city_country(self):
        formatted_address = city_country_fun("santiago","chile")
        self.assertEqual(formatted_address,"Santiago, Chile")

if __name__ == '__main__':
    unittest.main()
