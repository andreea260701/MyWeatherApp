# test_weather.py
import unittest
from pyweatherapp.weather import get_weather

class TestWeatherApp(unittest.TestCase):
    def test_valid_city(self):
        result = get_weather("London")
        self.assertIn("temperature", result)

    def test_invalid_city(self):
        result = get_weather("InvalidCityName")
        self.assertIn("error", result)

if __name__ == '__main__':
    unittest.main()
