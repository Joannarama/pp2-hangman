import random
from game_data import game_data


class Word:
    """This is the class for handling the words"""

    def __init__(self):
        self.game_word = self.get_word()
        self.guess = ''

    def get_word(self):
        """
        get the word for the user to use
        """
        return 'Oasis'
        category = random.choice(list(game_data.values()))
        return random.choice(category)

    def print_the_word(self, letters_used):
        """
        Prints the word for the user, if the user has guessed a letter show
        that letter, otherwise show an underscore
        """
        word_split = self.split_word_into_characters()

        word_output = ''

        for letter in word_split:
            # if  blank space add blank space
            if letter == ' ':
                word_output += '  '
            elif letter.lower() == self.guess:
                word_output += letter + ' '
            elif letter.lower() in letters_used:
                word_output += letter + ' '
            else:
                word_output += '_ '

        print(word_output.strip() + "\n")

    def is_letter_in_word(self, guess):
        """ Check if a letter is in the game word """
        lower_case_game_word = [x.lower() for x in self.game_word]

        if guess.lower() in lower_case_game_word:
            return True
        else:
            return False

    def split_word_into_characters(self):
        """
        Take a word and split it into individual characters
        """
        return [char for char in self.game_word]
