import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import add, divide, subtract


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(-2, 3), -5)
        self.assertEqual(subtract(-2, -3), 1)
        self.assertEqual(subtract(-1, -1), 0)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(1, 2), 0.5)
        self.assertEqual(divide(0, 2), 0)
        self.assertEqual(divide(-2, 2), -1)
        self.assertRaises(ValueError, divide, 6, 0)


if __name__ == "__main__":
    unittest.main()
