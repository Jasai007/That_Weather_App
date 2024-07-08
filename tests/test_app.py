import unittest
from app import app

class WeatherAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Weather App', response.data)

    def test_weather_post(self):
        response = self.app.post('/', data=dict(city='London'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'London', response.data)

if __name__ == '__main__':
    unittest.main()
