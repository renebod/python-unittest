__author__ = 'renebod'

import unittest
from experiment import Greeter

class MyTestCase(unittest.TestCase):
    def test_default_greeting_set(self):
        greeter = Greeter()
        self.assertEqual(greeter.message, 'Hello world!')

if __name__ == '__main__':
    unittest.main()