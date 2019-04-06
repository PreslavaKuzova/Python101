letter_to_symbol_dict = {
    'a': 2,
    'b': 22,
    'c': 222,
    'd': 3,
    'e': 33,
    'f': 333,
    'g': 4,
    'h': 44,
    'i': 444,
    'j': 5,
    'k': 55,
    'l': 555,
    'm': 6,
    'n': 66,
    'o': 666,
    'p': 7,
    'q': 77,
    'r': 777,
    's': 7777,
    't': 8,
    'u': 88,
    'v': 888,
    'w': 9,
    'x': 99,
    'y': 999,
    'z': 9999,
}

def decode_letter(sequence):
    if len(sequence) > 3 and int(sequence[0]) in [i for i in range(2, 10) if i not in [7, 9]]:
        while len(sequence) > 3:
            sequence = sequence[:len(sequence) - 3]

    if len(sequence) > 4 and int(sequence[0]) in [7, 9]:
        while len(sequence) > 3:
            sequence = sequence[:len(sequence) - 4]

    current_letter_key = int(''.join(str(number) for number in sequence))

    for letter, key in letter_to_symbol_dict.items():
        if current_letter_key == key:
            return letter

def numbers_to_message(pressed_sequence):
    list_with_numbers = [digit for digit in pressed_sequence]
    message_to_decode = []
    
    index = 0
    while index < len(list_with_numbers):
        if list_with_numbers[index] in [-1, 0, 1]:
            message_to_decode.append(list_with_numbers[index])
            index += 1
            continue
        current_sequence = [list_with_numbers[index]]
        while True:
            if(index != (len(list_with_numbers) - 1) and list_with_numbers[index] == list_with_numbers[index + 1]):
                current_sequence.append(list_with_numbers[index])
                index += 1
            else:
                break
        message_to_decode.append(current_sequence)
        index+=1
    
    actual_message = ''
    index = 0
    
    while index < (len(message_to_decode)):
        
        if(message_to_decode[index] == 0):
            actual_message += ' '
            index += 1
            continue
        if(message_to_decode[index] == -1):
            index += 1
            continue
        if(index < (len(message_to_decode) - 1) and (message_to_decode[index] == 1)):
            actual_message += decode_letter(message_to_decode[index + 1]).upper()
            index += 1
            continue
        
        actual_message += decode_letter(message_to_decode[index])
        index += 1

    return actual_message

def encode_letter(sequence):
    pass

def message_to_numbers(message):
    pass