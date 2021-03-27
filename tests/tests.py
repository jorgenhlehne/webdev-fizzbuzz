import unittest
import json
from fizzbuzz import app
from fizzbuzz.functions import calculate_fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_fizzbuzz_display(self):
        response = self.app.get('/fizzbuzz')
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/fizzbuzz?count=10')
        self.assertEqual(response.status_code, 200)
        response_decoded = response.data.decode('utf8')
        response_json = json.loads(response_decoded)
        self.assertEqual(len(response_json['msg']), 10)
        response = self.app.get('/fizzbuzz?haunt=10')
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/fizzbuzz?count=string')
        self.assertEqual(response.status_code, 200)

    def test_fizzbuzz_change(self):
        pass

    def test_calculate_fizzbuzz(self):
        fizzbuzz_15 = [
            1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8,
            'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz'
        ]

        self.assertEqual(calculate_fizzbuzz(count=15), fizzbuzz_15)
        self.assertEqual(
            len(calculate_fizzbuzz(count=57)), 57
        )
        self.assertEqual(
            calculate_fizzbuzz(fizzcount=5, buzzcount=5)[4], 'FizzBuzz'
        )
        self.assertEqual(
            calculate_fizzbuzz(fizzcount=4, fizzname='Foo')[3], 'Foo'
        )
        self.assertEqual(
            calculate_fizzbuzz(fizzcount=10, fizzname='Foo')[9], 'FooBuzz'
        )
        with self.assertRaises(TypeError):
            calculate_fizzbuzz(fizzcount='fizz')
