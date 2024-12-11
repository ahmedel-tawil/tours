from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    def test_add_two_numbers(self):
        """Test adding two numbers"""
        print('testing adding two numbers')
        res = calc.add(2, 4)
        self.assertEqual(res, 6)


    def test_subtract_two_numbers(self):
        """Test subtracting two numbers"""
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
