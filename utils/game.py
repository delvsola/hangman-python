from typing import List, Any
from random import choice


def transpose_element(first_list: List[str], second_list: List[str], element: Any) -> None:
    """
    Place the element in the second list at the indices it was at in the first list
    :param first_list: List to get the indices from
    :param second_list: List to transpose the element to
    :param element: Element to find and transpose
    :return: None
    """
    indices = [i for i, x in enumerate(first_list) if x == element]
    for index in indices:
        tmp = first_list[index]  # Swap buffer
        first_list[index] = second_list[index]
        second_list[index] = tmp


class Hangman:
    def __init__(self):
        self.possible_words: List[str] = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find: List[str] = []
        self.lives: int = 5
        self.correctly_guessed_letters: List[str] = []
        self.wrongly_guessed_letters: List[str] = []
        self.turn_count: int = 0
        self.error_count: int = 0

    def play(self):
        guess: str = input("Enter a single letter: ")
        if len(guess) != 1:
            print("Invalid input, try again.")
            return
        guess = guess.upper()  # Sanitize input
        if guess in self.correctly_guessed_letters or guess in self.wrongly_guessed_letters:
            print("You've already submitted this letter. Try again.")
            return
        elif guess in self.word_to_find:
            transpose_element(self.word_to_find, self.correctly_guessed_letters, guess)
        else:
            print("Incorrect guess :(")
            self.error_count += 1
            self.lives -= 1
            self.wrongly_guessed_letters.append(guess)

    def start_game(self):
        """Initialize the Hangman game and start it"""
        self.word_to_find = list(choice(self.possible_words).upper())
        self.correctly_guessed_letters = ["_"] * len(self.word_to_find)
        while True:
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
                print(f"Incorrect guesses: {', '.join(self.wrongly_guessed_letters)}")

    @staticmethod
    def game_over():
        print("Game over...")

    def well_played(self):
        print(f"You found the word \"{self.word_to_find}\" in {self.turn_count} turns with {self.error_count} errors !")
