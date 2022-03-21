from word import Word
from game_data import hangman_level


class Hangman:
    """This is the class for handling the hangman gameplay"""

    def __init__(self):
        # number of tries a user has
        self.number_of_tries = 8

        # variable for number of guesses
        self.number_of_errors = 0

        # letters the user has tried
        self.letters_used = []

        # variable for our word or words
        self.word = Word()

        # has the user won
        self.has_won = False

    def play_game(self):
        """
        Game
        """
        while True:
            self.has_won = self.word.all_letters_guessed_correctly(self.letters_used)

            if self.has_won is True:
                self.game_completed()
                continue

            self.word.print_the_word(self.letters_used)

            guess = self.user_guess()

            if guess is not False:
                self.draw_hangman()

                tries_left = self.number_of_tries - self.number_of_errors

                print(f"number of tries left: {tries_left}")

                letters_used_string = ' '.join(map(str, self.letters_used))
                print(f"The letters used {letters_used_string}")

                if tries_left == 0:
                    self.game_over('failed', self.word.game_word)

    def user_guess(self):
        """
        Handles the user guess
        """
        self.word.guess = ''

        guess = input("Guess a Letter: ")

        guess = guess.lower()

        if self.validate_guess(guess) is False:
            print(
                "You have entered an incorrect character, enter only letters"
                )
            return False
        elif self.letter_already_used(guess):
            print("You have already used this letter")
            return False
        else:
            print(f"The letter you guessed is {guess}")

            self.word.guess = guess

            self.letters_used.append(guess)

            if self.word.is_letter_in_word(guess) is False:
                self.number_of_errors += 1
                print(f"The letter {guess} is not in the word!")
            else:
                print(f"The letter {guess} is in the word!")

            return guess

    def draw_hangman(self):
        """
        Draws the hangman
        """
        if self.number_of_errors == 0:
            print(hangman_level[0])
        else:
            print(hangman_level[self.number_of_errors])

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
            self.reset_game()
            self.play_game()

    def validate_guess(self, guess):
        """
        Validate the user input
        """
        if guess.isalpha():
            return True
        else:
            return False

    def letter_already_used(self, guess):
        """
        Check if the letter has already been used
        """
        if guess in self.letters_used:
            return True
        else:
            return False

    def reset_game(self):
        """ Reset the game """
        self.has_won = False
        self.number_of_errors = 0
        self.letters_used = []
        self.word.reset()

    def game_completed(self):
        """ The user has won the game"""
        print("Congratulations you have won the game")
        input("Press enter to play again")
        self.reset_game()
