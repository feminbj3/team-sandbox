
import unittest

from app import calculate_tax, get_discount, get_os


class TestApp(unittest.TestCase):
    def test_calculate_tax(self):
        self.assertEqual(calculate_tax(100), 20)

    def test_get_discount(self):
        self.assertEqual(get_discount(), 45)

    def test_get_os(self):
        self.assertEqual(get_os(), "Linux")


if __name__ == "__main__":
    unittest.main()
