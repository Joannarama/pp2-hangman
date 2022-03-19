class Word:
    """This is the class for handling the words"""

    def __init__(self):
        self.game_word = self.get_word()

    def get_word(self):
        """
        get the word for the user to use
        """
        # open the json file and extract a random item
        return 'Tom Cruise'

    def print_the_word(self):
        """
        Prints the word for the user, if the user has guessed a letter show
        that letter, otherwise show an underscore
        """
        word_split = self.split_word_into_characters()

        guessed_letter = 'T'

        word_output = ''

        for letter in word_split:
            # if  blank space add blank space
            if letter == ' ':
                word_output += '  '
            elif letter == guessed_letter:
                word_output += guessed_letter + ' '
            else:
                word_output += '_ '
   
        print(word_output.strip() + "\n")

    def split_word_into_characters(self):
        """
        Take a word and split it into individual characters
        """
        return [char for char in self.game_word]
