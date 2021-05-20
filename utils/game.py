from typing import List, Any
from random import choice


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
    play()
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

    def play(self):
        """
        Core mechanics of the game. Take a single input from the player.
        :return None
        """
        guess: str = input("\nEnter a single letter: ")
        if len(guess) != 1:
            print("Invalid input, try again.")
            return
        guess = guess.upper()  # Sanitize input
        if guess in self.correctly_guessed_letters \
                or guess in self.wrongly_guessed_letters:
            print("You've already submitted this letter. Try again.")
            return
        elif guess in self.word_to_find:
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
        while self.is_over is False:
            if self.lives == 0:
                self.game_over()
                break
            elif "_" not in self.correctly_guessed_letters:
                self.well_played()
                break
            else:
                self.turn_count += 1
                self.play()
                print(f"Word: {''.join(self.correctly_guessed_letters)}")
                print(f"Incorrect guesses: "
                      f"{', '.join(self.wrongly_guessed_letters)}")

    def game_over(self):
        """
        Print the game over message.
        :return None
        """
        print("Game over...")
        self.is_over = True

    def well_played(self):
        """
        Print the success message.
        :return None
        """
        print(f"You found the word \"{''.join(self.word_to_find)}\" "
              f"in {self.turn_count} turns with {self.error_count} errors !")
