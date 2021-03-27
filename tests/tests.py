import unittest
from fizzbuzz import app

class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_url(self):
        pass

    def test_fizzbuzz_function(self):
        pass