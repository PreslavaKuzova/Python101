import sys
def cat(arguments):
    text_file = open(arguments[1], 'r')
    print(text_file.readlines())
    text_file.close()

def cat2(arguments):
    for file in arguments[1::]:
        text_file = open(file, 'r')
        print(text_file.readlines(), '\n')
        text_file.close()

from random import randint
def generate_numbers(filename, numbers):
    text_file = open(filename, 'w')
    for number in range(numbers):
        text_file.write(str(randint(1, 1000)) + ' ')
    text_file.close()

def sum_numbers_from_a_file(filename):
    sum = 0
    with open(filename,'r') as text_file:
        for line in text_file:
            for number in line.split():
                sum += int(number)
    print(sum)

def wc (parameter, command):
    characters = 0
    words = 0
    lines = 0
    text_file = open(parameter,'r')

    for line in text_file:
        lines = lines + 1
        words = words + len(line.split())
        characters = characters + len(line)

    if command == 'chars':
        return characters
    if command == 'words':
        return words
    return lines

def main():
    cat(sys.argv)
    cat2(sys.argv)
    generate_numbers('random_numbers.txt', 100)
    sum_numbers_from_a_file('random_numbers.txt')
    print(wc('story.txt', 'words'))
    print(wc('story.txt', 'lines'))
    print(wc('story.txt', 'chars'))

if __name__ == '__main__':
    main()
