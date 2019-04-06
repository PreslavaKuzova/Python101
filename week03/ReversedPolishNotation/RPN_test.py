import unittest 
from RPN import rpn_calculate

class TestReversedPolishNotation(unittest.TestCase):
    def test_when_single_digit_is_passed_then_return_the_same_digit(self):
        expr = '45'
        expected_result = 45
        self.assertEqual(rpn_calculate(expr), expected_result)

    def test_if_two_numbers_are_passed_then_return_sum_of_them(self):
        expression = '4 8 +'
        expected_result = 12
        self.assertEqual(rpn_calculate(expression), expected_result)

    def test_when_operator_is_substraction_of_two_numbers_then_return_the_difference(self):
        expression = '7 3 -'
        expected_result = 4
        self.assertEqual(rpn_calculate(expression), expected_result)

    def test_when_operator_is_multiplication_of_two_numbers_then_return_their_product(self):
        expression = '7 5 *'
        expected_result = 35
        self.assertEqual(rpn_calculate(expression), expected_result)

    def test_when_operator_is_division_of_two_numbers_then_return_their_division(self):
        expression = '6 3 /'
        expected_result = 2
        self.assertEqual(rpn_calculate(expression), expected_result)

    def test_when_there_are_three_consequtive_numbers_and_two_operators_then_return_result(self):
        expression = '7 5 9 + -'
        expected_result = -7
        self.assertEqual(rpn_calculate(expression), expected_result)

if __name__ == '__main__':
    unittest.main()