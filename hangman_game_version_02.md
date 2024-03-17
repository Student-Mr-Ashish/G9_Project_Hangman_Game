Here Ashish(developer) has uploded 2nd version of game. Here is some description of game

Now the game is complete and the developer has checked and corrected all the mistakes in the game.

Constants:

HANGMAN_PICS: A list of ASCII art representing the different stages of the hangman as the player makes incorrect guesses.
words_list: A list of words that could be selected as the secret word for the game.

Functions:
random_words(words): Selects a random word from the words_list.

display_screen(missed_letters, correct_letters, secret_word): Displays the current state of the game, including missed letters, correct letters guessed, and the word with blanks representing unguessed letters.

_guess(already_guessed): Handles user input for guessing letters. Ensures the input is a single alphabet that hasn't been guessed before.

play_again(): Asks the player if they want to play again.

Main Game Loop:

1.The game starts by selecting a random word from words_list.
2.Inside the game loop, it displays the current state of the game using    display_screen.
3.It then prompts the player to enter a guess using _guess.
4.If the guess is correct, it updates correct_letters and checks if the player has won.
5.If the guess is incorrect, it updates missed_letters and checks if the player has lost.
6.If the game is over (either won or lost), it asks the player if they want to play again.
7.The game continues until the player decides not to play again.

Execution:

1.The code begins by printing the title of the game.
2.Then, it initializes variables for missed letters, correct letters, and selects a secret word.
3.The main game loop runs until the player decides not to play again.

Overall:

This code creates a simple command-line Hangman game where the player guesses letters to uncover a hidden word. It provides feedback on missed letters and the current state of the word being guessed. If the player runs out of guesses, they lose, and if they guess the word correctly, they win. After each game, the player is given the option to play again.
