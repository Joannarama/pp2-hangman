def start_game():
    """
    User selects an option to begin or see rules
    """
    print("Welcome to Hangman")
    print("Please select option 1 or 2 to start")

    print("1. Game Rules")
    print("2. Play the Game")

    choice = input("Press 1 or 2 and press enter: ")

    if (choice == "1"):
        game_rules()
    elif (choice == "2"):
        play_game()    
    else:
        print("Please make a valid selection: 1 or 2")    
        start_game()

def game_rules():
    """
    Game Rules
    """
    print("game rules")

def play_game():
    """
    Game
    """
    print("play game")    

def user_guess():
    """
    Handles the user guess
    """
    guess = input("Guess a Letter: ")
    # validate the letter selection by the user
    print(f"The letter you guessed is {guess}")

start_game()

