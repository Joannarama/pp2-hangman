from hangman import Hangman


class Game:
    """ The class that controls the game """

    def __init__(self):
        self.hangman = Hangman()

    def start_game(self):
        """
        User selects an option to begin or see rules
        """
        print("Welcome to Hangman")
        print("\nPlease select option 1 or 2 to start")

        print("\n1. Game Rules")
        print("2. Play the Game")

        choice = input("\nPress 1 or 2 and press enter: ")

        if choice == "1":
            self.game_rules()
        elif choice == "2":
            self.hangman.play_game()
        else:
            print("\nPlease make a valid selection: 1 or 2  \n")
            self.start_game()

    def game_rules(self):
        """
        Game Rules
        """
        print("\nRULES")
        print("\nThe computer will select a secret word(s)")
        print("\nYou will see the number of letters you need to discover")
        print("\nMake your guess and the computer will tell if its right/wrong")
        print("\nGuess all the letters correctly before the hangman drops!\n")
        input("\nPress enter key to start\n\n")

        self.hangman.play_game()


game = Game()
game.start_game()
