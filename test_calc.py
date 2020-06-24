import unittest
import calc

class TestCalc(unittest.TestCase):
    def add(self):
        result = calc.add(5, 6)
        self.assertEqual(result, 11)

if __name__ == "__main__":
    unittest.main()