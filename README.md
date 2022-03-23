# Project Portfolio  - Python Essentials submission - Hangman Game

Hangman101 is a Python terminal game, which runs on the Code Institute mock terminal on Heroku.
The aim of the game is to try to guess all the letters of a secret word chosen at random by the computer. The user has a limited number of tries. If they fail to guess all the correct letters within the set number of tries, they will fail and they can play again. If they guesss the correct letters within the set number of tries, the user will have won!
It's intended audience is anyone who wants a mental break or to decompress from a stressful programming situation! 

## Repository
[Github repository](https://github.com/Joannarama/the-Oracle)

## Live site

## Table of Contents

- [User Experience (UX)](#user-experience)
  - [User Stories](#user-stories)

- [Features](#features)
- [How to play](#how-to-play)
- [Gameplay](#gameplay-area)

- [Technologies used](#technologies-used)
- [Languages](#languages-used)









![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Joannarama,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!