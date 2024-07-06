import unittest
from app.routes import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_screenshot_route(self):
        response = self.app.get('/screenshot')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('filename', data)
        self.assertIn('image', data)

    def test_webcam_route(self):
        response = self.app.get('/webcam')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('filename', data)
        self.assertIn('image', data)
'''
    def test_systeminfo_route(self):
        response = self.app.get('/systeminfo')
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/plain', response.content_type)
'''

if __name__ == '__main__':
    unittest.main()
