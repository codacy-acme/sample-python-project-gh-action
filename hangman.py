# Python Game with Unit Tests

import unittest
from unittest.mock import patch
from io import StringIO

def start_game(player_name):
    print(f"Welcome, {player_name}, to the Hangman Game!")

    word_list = ["apple", "banana", "cherry", "grape", "watermelon"]
    secret_word = random.choice(word_list)
    attempts = 0
    max_attempts = 6

    guessed_letters = []

    while True:
        print("Guess the word:")
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_ "

        print(display_word)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts += 1

        if attempts >= max_attempts:
            print(f"Sorry, {player_name}! You've run out of attempts. The word was '{secret_word}'.")
            break

        if all(letter in guessed_letters for letter in secret_word):
            print(f"Congratulations, {player_name}! You've guessed the word '{secret_word}'!")
            break

class TestHangmanGame(unittest.TestCase):
    @patch('builtins.input', side_effect=['a', 'b', 'c', 'd', 'e', 'f'])
    def test_game_wins(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            start_game("Test Player")
            output = mock_stdout.getvalue()
        self.assertIn("Congratulations, Test Player! You've guessed the word", output)

    @patch('builtins.input', side_effect=['x', 'y', 'z', 'p', 'q', 'r'])
    def test_game_loses(self, mock_input):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            start_game("Test Player")
            output = mock_stdout.getvalue()
        self.assertIn("Sorry, Test Player! You've run out of attempts.", output)

if __name__ == "__main__":
    import random
    name = input("Enter your name: ")
    start_game(name)

