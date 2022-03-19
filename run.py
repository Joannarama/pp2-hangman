from word import Word


def start_game():
    """
    User selects an option to begin or see rules
    """
    print("Welcome to Hangman")
    print("Please select option 1 or 2 to start")

    print("1. Game Rules")
    print("2. Play the Game")

    choice = input("Press 1 or 2 and press enter: ")

    if choice == "1":
        game_rules()
    elif choice == "2":
        play_game()
    else:
        print("\nPlease make a valid selection: 1 or 2  \n")
        start_game()


def game_rules():
    """
    Game Rules
    """
    print("game rules")

    input("Press enter key to start")
    play_game()


def play_game():
    """
    Game
    """
    print("play game")

    # number of tries a user has
    number_of_tries = 8

    # variable for number of guesses
    number_of_errors = 0

    # variable for our word or words
    word = Word()

    while True:
        word.print_the_word()

        user_guess()
        number_of_errors += 1

        draw_hangman(number_of_errors)

        print(f"number of tires {number_of_tries}")
        if number_of_errors > number_of_tries:
            game_over('failed', word.game_word)


def game_over(result, word):
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
        play_game()


def user_guess():
    """
    Handles the user guess
    """
    guess = input("Guess a Letter: ")
    # validate the letter selection by the user
    print(f"The letter you guessed is {guess}")


def draw_hangman(error):
    """
    Draws the hangman
    """
    error -= 1
    hangman_level = [
        """






           ----
        """,
        """

            |
            |
            |
            |
            |
           ----
        """,
        """
            ------
            |
            |
            |
            |
            |
           ----
        """,
        """
            ------
            |    |
            |
            |
            |
            |
           ----
        """,
        """
            ------
            |    |
            |    O
            |
            |
            |
           ----
        """,
        """
            ------
            |    |
            |    O
            |  --|--
            |
            |
           ----
        """,
        """
            ------
            |    |
            |    O
            |  --|--
            |   / \\
            |
           ----
        """,
        """
            ------
            |    |
            |    |
            |    O
            |  --|--
            |   / \\
           ----
        """
    ]

    print(hangman_level[error])


start_game()
