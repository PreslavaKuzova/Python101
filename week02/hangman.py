maximum_attempts = 10
def hangman(clue_word):
    tries = 0
    print('Welcome to Hangman! Let\'s play!')
    list_with_letters = [letter for letter in clue_word]
    list_to_use = ['_' for i in range(len(clue_word))]

    while tries < maximum_attempts:
        user_letter = input('Guess a letter: ')
        for index, letter in enumerate(list_with_letters):
            if user_letter == letter:
                list_to_use[index] = letter
        print(' '.join(list_to_use)) if(user_letter in list_with_letters) else print('Incorrect!')

        tries += 1

        if ('_' in list_to_use):
            continue
        else:
            break

    if(tries == 10):
        print('You lost! \n_________\n|    |    |\n|  \\ O /  |\n|    |    |\n|    |    |\n|   / \   |')

hangman('hello')