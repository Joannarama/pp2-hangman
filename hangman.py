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

        guess = input("Guess a Letter: \n")

        # makes guessed letter lower case for comparison against lowercase word
        guess = guess.lower()

        # ensure user choice is an alpha character and limited to one letter
        if self.validate_guess(guess) is False:
            print(
                "Incorrect character(s), enter only one letter"
                )
            return False
        elif self.letter_already_used(guess):
            # check if letter has already been used
            print("\nYou have already used this letter")
            return False
        else:
            # choice is correct, display letter in secret word
            print(f"The letter you guessed is {guess}")

            self.word.guess = guess

            # add the letter to the array of letters used
            self.letters_used.append(guess)

            # inform the user that their guess is correct or not
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
        # uses array from game_data.py to draw hangman character
        if self.number_of_errors == 0:
            print(hangman_level[0])
        else:
            print(hangman_level[self.number_of_errors])

    def game_over(self, result, word):
        """
        The game over status for a user
        """
        # notifies the user they have won
        if result == 'success':
            print("\nYou win!")
            input("\nPress enter to try again")

        # notifies the user they have failed
        else:
            print("\nYou lost!")
            print("\nThe correct answer was: " + word)
            input("\nPress enter to try again")
            self.reset_game()
            self.play_game()

    def validate_guess(self, guess):
        """
        Validate the user input
        """
        # ensures user inpur is alpha and only one character
        if guess.isalpha() and len(guess) == 1:
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
        # resets the game parameters to to start point
        self.has_won = False
        self.number_of_errors = 0
        self.letters_used = []
        self.word.reset()

    def game_completed(self):
        """ The user has won the game"""
        print("\nCongratulations you have won the game")
        input("\nPress enter to play again")
        self.reset_game()
