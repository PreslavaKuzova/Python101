def is_credit_card_valid(number):
    if len(str(number)) % 2 == 0:
        return False

    str_number = str(number)

    even_positions = [digit for digit in str_number[::2]]
    odd_positions = [str(int(digit)*2) for digit in str_number[1::2]]
    new_card_number =[int(digit) for digit in ''.join(even_positions + odd_positions)]

    if (sum(new_card_number)%10 == 0):
        return True
    return False