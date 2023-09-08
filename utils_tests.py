import unittest
from utils import Utils

class UtilTests(unittest.TestCase):
    def test_reversed_integer(self):
        self.assertEqual(Utils.reversed(12345), 54321)

    def test_reversed_float(self):
        with self.assertRaises(ValueError):
            Utils.reversed(12.34)

    def test_reversed_string(self):
        result = Utils.reversed('12345')
        self.assertEqual(result, 54321)
    
    def test_formatter_integer(self):
        binary, octal = Utils.formatter(10)
        self.assertEqual(binary, '0b1010')
        self.assertEqual(octal, '0o12')
    
    def test_formatter_float(self):
        with self.assertRaises(TypeError):
            Utils.formatter(12.34)

    def test_formatter_string(self):
        with self.assertRaises(TypeError):
            Utils.formatter("10")

if __name__ == '__main__':
    unittest.main()

