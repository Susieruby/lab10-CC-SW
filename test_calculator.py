import unittest
import calculator
#https://github.com/Susieruby/lab10-CC-SW
#Partner1: Cheuvront Cason Makail
#Partner2:Song Wenxi

class TestCalculator(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(calculator.mul(2, 3), 6)
        self.assertEqual(calculator.mul(-4, 5), -20)
        self.assertEqual(calculator.mul(0, 9), 0)

    def test_divide(self):
        self.assertEqual(calculator.div(2, 4), 2.0)
        self.assertEqual(calculator.div(5, 10), 2.0)
        with self.assertRaises(ZeroDivisionError):
            calculator.div(0, 7)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.log(0, 5)
        with self.assertRaises(ValueError):
            calculator.log(1, 10)
        with self.assertRaises(ValueError):
            calculator.log(-2, 3)
        with self.assertRaises(ValueError):
            calculator.log(2, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(-5, 12), 13.0)
        self.assertAlmostEqual(calculator.hypotenuse(0, 0), 0.0)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(16), 4.0)
        self.assertAlmostEqual(calculator.square_root(2), 1.41421356)
        with self.assertRaises(ValueError):
            calculator.square_root(-9)


if __name__ == "__main__":
    unittest.main()