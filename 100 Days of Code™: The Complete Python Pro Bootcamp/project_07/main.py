'''
Hangman Game – Code Documentation

Overview

This Python script implements a console-based version of the classic Hangman game.
The program randomly selects a word from an external word list and challenges the user
to guess it one letter at a time.

Game Flow

- The game starts by displaying a logo and initializing the number of lives.
- A random word is selected, and a placeholder is shown using underscores.
- The user is prompted to guess letters in a loop until they either win or lose.
- Correct guesses reveal the letter’s position(s) in the word.
- Incorrect guesses reduce the number of remaining lives.

Features

- Tracks correctly guessed letters and updates the display dynamically.
- Prevents repeated guesses from affecting gameplay.
- Displays remaining lives after each turn.
- Uses ASCII art stages to visually represent progress.
- Ends with a win or lose message, revealing the correct word if needed.

Modules Used

- random: for selecting a random word.
- hangman_words: contains the list of possible words.
- hangman_art: contains the game logo and visual stages.

This project demonstrates fundamental Python concepts such as loops, conditionals,
lists, string manipulation, and basic game logic.
'''

import random
import hangman_words
import hangman_art

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
word_list = hangman_words.word_list

lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
logo = hangman_art.logo
print(logo)
chosen_word = random.choice(word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f"You have already guessed the letter {guess}")


    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
    #  e.g. You guessed d, that's not in the word. You lose a life.

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True

            # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
            print(f"***********************YOU LOSE**********************\nThe correct word is {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(hangman_art.stages[lives])
