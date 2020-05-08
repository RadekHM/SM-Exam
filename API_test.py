"Test for Api"
import unittest
import requests

class TestMathFunction(unittest.TestCase):
    "Class to test Api"
    def test_api(self):
        "Tests for the api"
        url = "https://corona-virus-stats.herokuapp.com/api/v1/" \
              "cases/countries-search?search=Ukraine"
        test = requests.get(url)
        status_code = test.status_code
        expected = 200
        data = test.json()

        status = data["status"]
        status_message = "success"

        self.assertEqual(status_code, expected)
        self.assertEqual(status, status_message)


if __name__ == '_main_':
    unittest.main()