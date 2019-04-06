import math

def simplify_fraction(fraction):
    
    if not isinstance(fraction, tuple):
        raise Exception('You should give a tuple as an instance')
    if fraction[1] == 0:
        raise Exception('Division by zero not possible')
    if fraction[0] == fraction[1]:
        return (1, 1)

    common_divisor = gcd(fraction[0], fraction[1])
    return (fraction[0]//common_divisor, fraction[1]//common_divisor)

def collect_fractions(fractions):
    sum = fractions[0]
    for fraction in fractions[1:]:
        greatest_divider = gcd(fraction[1], sum[1])
        sum_list = list(sum)
        if greatest_divider == 1:
            sum_list[0] = fraction[0]*sum[1] + fraction[1]*sum[0]
            sum_list[1] = fraction[1]*sum[1]
            sum = tuple(sum_list)
            simplify_fraction(sum)
        else:
            lowest_multiple = lcm(fraction[1], sum[1])
            sum_list[0] = fraction[0]*(lowest_multiple//fraction[1])+ sum[0]*(lowest_multiple//sum[1])
            sum_list[1] = lowest_multiple
            sum = tuple(sum_list)
            simplify_fraction(sum)

def return_frac(s):
    return s[0]/s[1]

def sort_array_of_fractions(fractions):
    return sorted(fractions, key = return_frac)

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
def lcm(a, b):
    return a * b / gcd(a, b)
