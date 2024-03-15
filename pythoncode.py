import random

HANGMAN_PICS = ['''
    +---+
         |
         |
         |
        ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']
words_list = 'antelope bison buffalo chimpanzee elephant giraffe gorilla hippopotamus jaguar kangaroo koala leopard ostrich panther porcupine raccoon squirrel yak armadillo baboon bobcat cheetah hyena jackal'.split()

def random_words(words):
    """
    Returns a random word from the words listed above.
    """
    words_index = random.randint(0, len(words) - 1)
    return words[words_index]

def display_screen(missed_letters, correct_letters, secret_word):
    print()
    print(HANGMAN_PICS[len(missed_letters)])
    print()
    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:

    # Display the secret word with spaces between the letters:
    for letter in blanks:
        print(letter, end =' ')
    print()

def _guess(already_guessed):
    """
    Returns the alphabet that is entered by the player.
    Ensures that the player enters a single alphabet nothing else.
    """
    while True:
        print('Please guess an alphabet.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('please enter only a single alphabet.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter an alphabet nothing else.')
        else:
            return guess

