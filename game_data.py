""" Game data used for hangman """
game_data = {
    'actors': [
        'Tom Cruise'
    ],

    'places': [
        'London'
    ],

    'movies': [
        'Ghostbusters'
    ],

    'songs': [
        'Riverdance'
    ],

    'books': [
        'Harry Potter'
    ],

    'bands': [
        'Oasis'
    ],
}

hangman_level = [
    """







    """,
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
