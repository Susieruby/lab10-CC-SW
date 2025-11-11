#https://github.com/Susieruby/lab10-CC-SW
#Partner1: Cheuvront Cason Makail
#Partner2:Song Wenxi
import unittest
import calculator
import math

class TestCalculator(unittest.TestCase):
    # ---------------------- Partner 1  ----------------------
    def test_add(self):
        self.assertEqual(calculator.add(5, 3), 8)
        self.assertEqual(calculator.add(-2, 4), 2)
        self.assertEqual(calculator.add(0, 0), 0)
        self.assertEqual(calculator.add(1.5, 2.5), 4.0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(10, 4), 6)
        self.assertEqual(calculator.subtract(-3, -5), 2)
        self.assertEqual(calculator.subtract(7, 0), 7)
        self.assertAlmostEqual(calculator.subtract(4.2, 1.1), 3.1)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, -3)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 0.0)

    def test_logarithm(self):
        self.assertAlmostEqual(calculator.logarithm(2, 8), 3.0)
        self.assertAlmostEqual(calculator.logarithm(10, 1000), 3.0)
        self.assertAlmostEqual(calculator.logarithm(math.e, math.e ** 5), 5.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(0, 5)
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 20)

    # ---------------------- Partner 2 ----------------------
    def test_multiply(self):
        self.assertEqual(calculator.mul(2, 3), 6)
        self.assertEqual(calculator.mul(-4, 5), -20)
        self.assertEqual(calculator.mul(0, 9), 0)
        self.assertAlmostEqual(calculator.mul(2.5, 4), 10.0)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 4), 2.0)
        self.assertEqual(calculator.div(5, 10), 2.0)
        self.assertAlmostEqual(calculator.div(3, 6.0), 2.0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -5)
        with self.assertRaises(ValueError):
            calculator.logarithm(3, 0)
        with self.assertRaises(ValueError):
            calculator.logarithm(5, -10.5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(-5, 12), 13.0)
        self.assertAlmostEqual(calculator.hypotenuse(0, 0), 0.0)
        self.assertAlmostEqual(calculator.hypotenuse(6.0, 8.0), 10.0)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(16), 4.0)
        self.assertAlmostEqual(calculator.square_root(2), 1.41421356)
        self.assertEqual(calculator.square_root(0), 0.0)
        with self.assertRaises(ValueError):
            calculator.square_root(-9)

if __name__ == '__main__':
    unittest.main()