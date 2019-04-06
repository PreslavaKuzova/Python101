def anagrams (first, second):
    first_list = [letter.lower() for letter in first]
    second_list = [letter.lower() for letter in second]
    return first_list.sort() == second_list.sort()

first = input("Input the first word to check: ")
second = input("Input the second word to check: ")
print(anagrams(first, second))