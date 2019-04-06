import sys
import re
class Monomial:
    def __init__ (self, coefficient, power):
        self.coefficient = coefficient
        self.power = power

    def calculate_derivative(self):
        if self.power is not 0:
            self.coefficient *= self.power
            self.power -=1
            if self.power == 0:
                return str(self.coefficient)
        else:
            return str(0)
        return str(self.coefficient) + "x^" +str(self.power)

    @staticmethod
    def convert_into_monomial(str_to_split):
        
        if str_to_split.find('x') == -1:
            return Monomial(int(str_to_split), 0)

        lst = re.findall(r"[\w']+", ''.join(str_to_split.split('x')))
        if str_to_split[0] == 'x':
            lst = [1] + lst
        if len((str_to_split.split('x'))[1]) == 0:
            lst = lst + [1]
        lst = list(map(int, lst))
        
        return Monomial(lst[0], lst[1])

class Polynomial(Monomial):
    def __init__(self):
        array_of_string_monomials = (str(sys.argv[1])).split('+')
        self.array_of_monomials = []
        for string_monomial in array_of_string_monomials:
            current_monomial = Monomial.convert_into_monomial(string_monomial)
            self.array_of_monomials += [current_monomial]


    def print_polynomial_derivative(self):
        derivative = ''
        for index, monomial in enumerate(self.array_of_monomials):
            current_derivative = monomial.calculate_derivative()
            if current_derivative != '0':
                derivative += current_derivative
                if index != (len(self.array_of_monomials) - 2):
                    derivative += '+'
        print(derivative)

def main():
    p = Polynomial()
    p.print_polynomial_derivative()

if __name__ == '__main__':
    main()
