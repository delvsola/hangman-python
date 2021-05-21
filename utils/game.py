from typing import List, Any
from random import choice
import platform  # For getting the operating system name
import os

#  Contains each frame of the hangman
parts = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
         "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
         "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
         "  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
         "  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
         "  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n========="]


def clear_screen():
    """
    Clears the terminal screen.
    :return None
    """
    # Check which OS the user is running in order to execute the correct clear
    command = "cls" if platform.system().lower() == "windows" else "clear"
    # Execute the clear command
    os.system(command)


def transpose_element(first_list: List[str],
                      second_list: List[str], element: Any) -> None:
    """
    Place the element in the second list at the indices it was at in
        the first list
    :param first_list: List to get the indices from
    :param second_list: List to transpose the element to
    :param element: Element to find and transpose
    :return: None
    """
    # Build a list to store the position of all occurrences of element
    indices = [i for i, x in enumerate(first_list) if x == element]
    for index in indices:
        second_list[index] = first_list[index]


class Hangman:
    """
    Starts and manage a game of Hangman

    ...

    Attributes
    ----------
    possible_words : List[str]
        contains the possible words to guess
    word_to_find : List[str]
        list of single characters that make up the chosen word to guess
    lives : int
        number of lives left
    correctly_guessed_letters : List[str]
        contains the correctly guessed letters at their correct position
    wrongly_guessed_letters : List[str]
        contains the incorrectly guessed letters
    turn_count : int
        current number of turns played
    error_count : int
        current number of wrong guesses made during the game
    is_over : bool
        if the game is over due to too many errors or not
    Methods
    -------
    start_game()
        Initializes the Hangman game and starts the game loop.
    """

    def __init__(self):
        self.possible_words: List[str] = ['becode',
                                          'learning',
                                          'mathematics',
                                          'sessions',
                                          'python',
                                          'coding',
                                          'programming',
                                          'github']
        self.word_to_find: List[str] = []
        self.lives: int = 5
        self.correctly_guessed_letters: List[str] = []
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0
        self.is_over = False

    def __play(self):
        """
        Core mechanics of the game. Take a single input from the player.
        :return None
        """
        guess: str = input("\nEnter a single letter: ")
        clear_screen()  # Clear the screen to refresh it
        if len(guess) != 1:
            print("Invalid input, try again.")
            return
        guess = guess.upper()  # Sanitize input
        if guess in self.correctly_guessed_letters \
                or guess in self.wrongly_guessed_letters:
            print("You've already submitted this letter. Try again.")
            return
        elif guess in self.word_to_find:
            print("Nice guess !")
            transpose_element(
                self.word_to_find,
                self.correctly_guessed_letters,
                guess
            )
        else:
            print("Incorrect guess :(")
            self.error_count += 1
            self.lives -= 1
            self.wrongly_guessed_letters.append(guess)

    def start_game(self):
        """
        Initialize the Hangman game and start the game loop
        :return None
        """
        self.word_to_find = list(choice(self.possible_words).upper())
        self.correctly_guessed_letters = ["_"] * len(self.word_to_find)
        clear_screen()  # Clear the screen to prettify the game
        print("Welcome to the Hangman, will you guess the word ?")
        while self.is_over is False:
            print(parts[self.error_count])
            print(f"Word: {''.join(self.correctly_guessed_letters)}")
            print(f"Incorrect guesses: "
                  f"{', '.join(self.wrongly_guessed_letters)}")
            if self.lives == 0:
                self.__game_over()
                break
            elif "_" not in self.correctly_guessed_letters:
                self.__well_played()
                break
            else:
                self.turn_count += 1
                self.__play()

    def __game_over(self):
        """
        Print the game over message.
        :return None
        """
        print(f"Game over... The word was {''.join(self.word_to_find)}")
        self.is_over = True

    def __well_played(self):
        """
        Print the success message.
        :return None
        """
        print(f"You found the word \"{''.join(self.word_to_find)}\" "
              f"in {self.turn_count} turns with {self.error_count} errors !")
