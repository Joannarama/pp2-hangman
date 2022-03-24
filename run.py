""" Run the application """
from hangman import Hangman
from bcolors import Bcolors


class Game:
    """ The class that controls the game """

    def __init__(self):
        self.hangman = Hangman()

    def start_game(self):
        """
        User selects an option to begin or see rules
        """
        self.hangman.hangman_title()
        print("Please select option 1 or 2 to start")
        print("\n")
        print("1. Game Rules")
        print("2. Play the Game")
        print("Press 1 or 2 and press enter: ")
        choice = input("")

        if choice == "1":
            self.hangman.clear_screen()
            self.hangman.hangman_title()
            self.game_rules()
        elif choice == "2":
            self.hangman.play_game()
        else:
            self.hangman.clear_screen()
            self.hangman.hangman_title()
            print("Please make a valid selection: 1 or 2")
            self.start_game()

    def game_rules(self):
        """
        Game Rules
        """
        print(f"{Bcolors.UNDERLINE}Rules{Bcolors.ENDC}")
        print("\n")
        print("The computer will select a secret word(s)")
        print(
            "You will see the number of letters you need to discover"
        )
        print(
            "Make a guess and the computer will tell if its right/wrong"
        )
        print(
            "Guess all the letters correctly before the hangman drops!"
            )
        print("\n")
        print(
            f"{Bcolors.OKBLUE}Press ENTER key to start{Bcolors.ENDC}"
        )
        input("")

        self.hangman.play_game()


game = Game()
game.start_game()
