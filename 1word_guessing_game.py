# word_guessing_game.py

import random

# README
# Selects a random word from the list
def choose_word():
    words = ['apple', 'banana', 'mango', 'watermelon', 'orange']
    return random.choice(words)

# README
# Takes the secret word and the list of guessed letters as input
# Represents the string
def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

# READ ME
# Tracks the number of turns and word guesses made by the player
# Allows the player to guess a letter of the whole word
# Ends the game when the word is guessed coreectly 
def play_game():
    secret_word = choose_word()
    guessed_letters = []
    guessed_words = []
    turns = 0
    max_turns = 10

    print("Welcome to the Word Guessing Game!")
    print("The word has {} letters.".format(len(secret_word)))
    print(display_word(secret_word, guessed_letters))

    while turns < max_turns:
        guess = input("Guess a letter or the whole word: ").lower()

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed that letter.")
            else:
                guessed_letters.append(guess)
                turns += 1
                if guess in secret_word:
                    print("Correct!")
                else:
                    print("Incorrect.")
        else:
            if guess == secret_word:
                print("Congratulations! You guessed the word.")
                break
            else:
                print("Incorrect word guess.")
                turns += 1

        print(display_word(secret_word, guessed_letters))

    if turns == max_turns:
        print("You've run out of turns. The word was '{}'.".format(secret_word))

if __name__ == "__main__":
    play_game()
