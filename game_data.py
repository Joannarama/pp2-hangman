""" Game data used for hangman """
game_data = {
    'actors': [
        'Tom Cruise'
        'Ben Affleck'
        'Jodie Foster'
        'Meryl Streep'
        'Emma Watson'
    ],

    'places': [
        'London'
        'Dublin'
        'Paris'
        'New York'
        'Beijing'
    ],

    'movies': [
        'Ghostbusters'
        'Zoolander'
        'Oceans Eleven'
        'Batman'
        'Sing'
    ],

    'fruit': [
        'banana'
        'peache'
        'apple'
        'orange'
        'coconut'
    ],

    'books': [
        'Harry Potter'
        'Dr Zhivago'
        'The Hobbit'
        'A Tale of Two Cities'
        'Anne Frank'

    ],

    'bands': [
        'Oasis'
        'Blur'
        'Queen'
        'The Beatles'
        'The Rolling Stones'
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
