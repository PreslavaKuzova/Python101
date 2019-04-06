import unittest
from simplify_fraction import simplify_fraction, gcd, collect_fractions, lcm, sort_array_of_fractions

class TestSimplifyFraction(unittest.TestCase):
    def test_when_the_denominator_is_zero(self):
        expr = (1, 0)
        self.assertRaises(Exception, simplify_fraction(expr))

    def test_validate_fraction_object_is_a_tuple(self):
        expr = [1, 2]
        self.assertRaises(Exception, simplify_fraction(expr))
    
    def test_when_the_number_is_not_imaculate_then_return_the_gcd(self):
        expr = (7, 21)
        expected_result = 7
        self.assertEqual(gcd(expr[0], expr[1]), expected_result)

    def test_when_the_nominator_is_not_prime_but_the_number_is(self):
        expr = (4, 7)
        expected_result = (4, 7)
        self.assertEqual(simplify_fraction(expr), expected_result)

    def test_when_the_denominator_is_not_prime_but_the_number_is(self):
        expr = (3, 8)
        expected_result = (3, 8)
        self.assertEqual(simplify_fraction(expr), expected_result)

    def test_when_the_nominator_and_the_denominator_are_equal(self):
        expr = (4, 4)
        expected_result = (1, 1)
        self.assertEqual(simplify_fraction(expr), expected_result)

    def test_when_number_is_not_imaculate_then_return_the_simplified_number1(self):
        expr = (3, 9)
        expected_result = (1, 3)
        self.assertEqual(simplify_fraction(expr), expected_result)

    def test_when_number_is_not_imaculate_then_return_the_simplified_number2(self):
        expr = (63,462)
        expected_result = (3,22)
        self.assertEqual(simplify_fraction(expr), expected_result)

    def test_when_number_is_not_imaculate_then_return_the_simplified_number3(self):
        expr = (5, 6)
        expected_result = (5, 6)
        self.assertEqual(simplify_fraction(expr), expected_result)

    def test_the_lowest_common_multiple_of_two_imaculate_numbers1(self):
        expected_result = 72
        self.assertEqual(lcm(8, 9), expected_result)

    def test_the_lowest_common_multiple_of_two_numbers(self):
        expected_result = 15
        self.assertEqual(lcm(5, 15), expected_result)

    def test_sorting_of_array_of_fractions(self):
        expected_result = [(1, 1000), (1, 100), (1, 10)]
        self.assertEqual(sort_array_of_fractions(
            [(1, 100), (1, 10), (1, 1000)]), expected_result)

if __name__ == '__main__':
    unittest.main()
