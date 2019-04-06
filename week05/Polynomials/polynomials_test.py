import unittest 
from polynomials import Monomial

class TestPolynomials(unittest.TestCase):
    def test_the_calcualtion_of_a_derivative(self):
        expr = Monomial(3, 4)
        expected_result = '12x^3'
        self.assertEqual(expr.calculate_derivative(), expected_result)
    
    def test_the_calcualtion_of_a_derivative_when_the_power_is_zero(self):
        expr = Monomial(3, 0)
        expected_result = '0'
        self.assertEqual(expr.calculate_derivative(), expected_result)
    
    def test_the_calcualtion_of_a_derivative_when_the_power_is_one(self):
        expr = Monomial(3, 1)
        expected_result = '3'
        self.assertEqual(expr.calculate_derivative(), expected_result)

    def test_converting_into_monomial(self):
        expr = '12x^3'
        expected_result = Monomial(12, 3)
        self.assertEqual(Monomial.convert_into_monomial(expr).coefficient, expected_result.coefficient)

    def test_converting_into_monomial_when_the_given_expression_is_a_constant(self):
        expr = '12'
        expected_result = Monomial(12, 0)
        self.assertEqual(Monomial.convert_into_monomial(expr).power, expected_result.power)

    def test_converting_into_monomial_when_the_coefficient_is_1(self):
        expr = 'x^3'
        expected_result = Monomial(1, 3)
        self.assertEqual(Monomial.convert_into_monomial(expr).coefficient, expected_result.coefficient)

    def test_converting_into_monomial_when_the_power_is_1(self):
        expr = '12x'
        expected_result = Monomial(12, 1)
        self.assertEqual((Monomial.convert_into_monomial(expr)).power, expected_result.power)

    def test_converting_into_monomial_when_both_coefficient_and_power_are_1(self):
        expr = 'x'
        expected_result = Monomial(1, 1)
        self.assertEqual(Monomial.convert_into_monomial(expr).coefficient, expected_result.coefficient)

if __name__ == '__main__':
    unittest.main()