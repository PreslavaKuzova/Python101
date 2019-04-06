import re
def sum_of_numbers(input_string):
    list_with_numbers = re.findall("[\d]+", input_string)
    sum = 0
    for number in list_with_numbers:
        sum += int(number)

    return sum 