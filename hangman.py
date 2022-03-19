from word import Word
from game_data import hangman_level


class Hangman:
    """This is the class for handling the hangman gameplay"""

    def play_game(self):
        """
        Game
        """

        # number of tries a user has
        number_of_tries = 8

        # variable for number of guesses
        number_of_errors = 0

        # variable for our word or words
        word = Word()

        while True:
            word.print_the_word()

            self.user_guess()
            number_of_errors += 1

            self.draw_hangman(number_of_errors)

            print(f"number of tires {number_of_tries}")
            if number_of_errors > number_of_tries:
                self.game_over('failed', word.game_word)

    def user_guess(self):
        """
        Handles the user guess
        """
        guess = input("Guess a Letter: ")
        # validate the letter selection by the user
        print(f"The letter you guessed is {guess}")

    def draw_hangman(self, error):
        """
        Draws the hangman
        """
        error -= 1       
        print(hangman_level[error])

    def game_over(self, result, word):
        """
        The game over status for a user
        """
        if result == 'success':
            print("You win!")
            input("Press enter to try again")
        else:
            print("You lost!")
            print("The correct answer was: " + word)
            input("Press enter to try again")
            self.play_game()
