import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    def test_addtion(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -5), -6)
    def test_subtruction(self):
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(4, 1), 3)
        self.assertEqual(self.calc.subtract(-1, -5), 4)
        self.assertEqual(self.calc.subtract(-1, 5), -6)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-6, 4), -24)
        self.assertEqual(self.calc.multiply(-2, -5), 10)
        self.assertEqual(self.calc.multiply(2, 0), 0)
    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-15, -5), 3)
        self.assertEqual(self.calc.divide(14, 0), None)
    