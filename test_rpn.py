import unittest
import rpn


class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
    def test_adds(self):
        result = rpn.calculate('1 1 + 2 +')
        self.assertEqual(4, result)
    def test_subtract(self):
        result = rpn.calculate('5 2 -')
        self.assertEqual(3, result)
    def test_toomany(self):
        with self.assertRaises(TypeError):
            result = rpn.calculate('1 2 3 +')
    def test_mult(self):
        result = rpn.calculate('3 2 *')
        self.assertEqual(6, result)
    def test_div(self):
        result = rpn.calculate('6 3 /')
        self.assertEqual(2, result)
    def test_multiple_operators(self):
        result = rpn.calculate('2 10 * 5 8 * + 3 /')
        self.assertEqual(20, result)
    def test_factorial(self):
        result = rpn.calculate('4 !')
        self.assertEqual(24, result)
    def test_zero_div(self):
        result = rpn.calculate('1 2 + 8 0 /')
        self.assertEqual(3, result)
    def test_summation(self):
        result = rpn.calculate('1 2 3 4 5 ++')
        self.assertEqual(15, result)


