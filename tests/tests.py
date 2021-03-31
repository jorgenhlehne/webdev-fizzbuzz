import unittest
import json
from fizzbuzz import app, db
from fizzbuzz.models import Variables
from fizzbuzz.functions import calculate_fizzbuzz


class TestFizzBuzz(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

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
        response = self.app.get('/fizzbuzz/change')
        self.assertEqual(response.status_code, 200)
        response = self.app.get('/fizzbuzz/change?fizz_count=Foo')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(
            db.session.query(Variables).filter_by(id=1).first().fizz_count,
            'Foo'
        )
        response = self.app.get('/fizzbuzz/change?fizz_count=4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            db.session.query(Variables).filter_by(id=1).first().fizz_count,
            4
        )
        response = self.app.get('/fizzbuzz/change?fizz_name=Foo')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            db.session.query(Variables).filter_by(id=1).first().fizz_name,
            'Foo'
        )
        response = self.app.get('/fizzbuzz/change?buzz_count=6')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            db.session.query(Variables).filter_by(id=1).first().buzz_count,
            6
        )
        response = self.app.get('/fizzbuzz/change?buzz_name=Bar')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            db.session.query(Variables).filter_by(id=1).first().buzz_name,
            'Bar'
        )

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
            calculate_fizzbuzz(fizz_count=5, buzz_count=5)[4], 'FizzBuzz'
        )
        self.assertEqual(
            calculate_fizzbuzz(fizz_count=4, fizz_name='Foo')[3], 'Foo'
        )
        self.assertEqual(
            calculate_fizzbuzz(fizz_count=10, fizz_name='Foo')[9], 'FooBuzz'
        )
        self.assertEqual(
            calculate_fizzbuzz(fizz_name='Foo', buzz_name='Bar')[14], 'FooBar'
        )
        with self.assertRaises(TypeError):
            calculate_fizzbuzz(fizz_count='fizz')
