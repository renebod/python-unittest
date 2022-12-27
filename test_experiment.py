__author__ = 'rene.bod@mac.com'

import unittest
from math import pi
from experiment import Greeter, Calculator


class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = Greeter()
        self.assertEqual(greeter.message, 'Hello world!')
    
    def test_calculate_area(self):
        area = Calculator.calculate_area(17)
        self.assertEqual(area, pi * 289)

    def test_calculate_area_type(self):
        area = Calculator.calculate_area(17)
        self.assertIsInstance(area, float)

if __name__ == '__main__':
    unittest.main()