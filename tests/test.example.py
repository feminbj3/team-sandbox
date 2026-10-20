
import unittest

class ExampleTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 3, 5)

    def test_string(self):
        self.assertEqual("hello".upper(), "HELLO")

if __name__ == "__main__":
    unittest.main()
