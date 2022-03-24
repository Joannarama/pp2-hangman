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
        print("Please select option 1 or 2 to start")

        print("1. Game Rules")
        print("2. Play the Game")

        choice = input("Press 1 or 2 and press enter: ")

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
        print("\nThe computer will select a secret word at random \nYou have 8 tries to guess all the correct letters! \nGood luck :)")

        input("\nPress enter key to start\n")

        self.hangman.play_game()


game = Game()
game.start_game()
