# test_my_module.py

import unittest
from my_module import add_numbers

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        # Test adding two positive numbers
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_numbers(self):
        # Test adding two negative numbers
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_add_mixed_numbers(self):
        # Test adding a positive and a negative number
        self.assertEqual(add_numbers(-2, 3), 1)

if __name__ == "__main__":
    unittest.main()
