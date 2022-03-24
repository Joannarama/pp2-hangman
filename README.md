# **Project Portfolio  - Python Essentials submission - Hangman Game**

## **Overview**

Hangman is a Python terminal game, which runs on a mock terminal which is viewed on Heroku.

The aim of the game is to try to guess all the letters of a secret word chosen at random by the computer. The user has a limited number of tries. If they fail to guess all the correct letters within the set number of tries, they will lose that round of the game and they can try  again. If they guesss the correct letters within the set number of tries, the user will have won!
It's intended audience is anyone who wants a mental break or to decompress from a stressful programming situation! 

## Repository
[Github repository](https://github.com/Joannarama/the-Oracle)

## Live site

## Table of Contents

- [Scoping Phase](#scoping-phase)
  - [User Stories](#user-stories)
  - [Site Owner Objectives](#site-owner-objectives)
  - [How Objectives will be achieved](#how-the-objectives-will-be-achieved)
  - [Features](#features)

- [Planning](#planning)

- [Features](#features)
  -[Landing Page](#landing-page)


- [How to play](#how-to-play)
- [Gameplay](#gameplay-area)

- [Technologies used](#technologies-used)
- [Languages](#languages-used)




# **Scoping phase**

## ***User Stories***
* As a user I want to quickly and easily understand how to play the game
* As a user I want to have a positive response to my interaction with the game
* As a user to have a leisurely engagement with a fun game

## ***Site Owner Objectives***
* As a site owner, I want the user to play an enjoyable game
* As a site owner, I want the user to understand easily how to initiate and proceed through the game
* As a site owner, I want the user to have a positive engagement with the game

## ***How the Objectives will be achieved***
The objectives will be achieved by 
* Offering clear instructions on how to play
* Indicating what action the user must take at each step
* Notifying the user if they have made an error
* Counting down the tries remaining for the user
* Congratulate them if they have won or encourage to play again if they lost

# **Planning**
I created a flowchart in Lucid chart to help organise the structure of the game and my approach to it's development

![planning flowchart](docs/images/flowchart.jpeg)

# **Features**

## ***Landing Page***
On the landing page, the user sees the Welcome to Hangman title and is prompted to choose an option:
1. Rules 
2. Game

![landing page](docs/images/landing_page.jpg)

### User selects 1

When the user selects choice 1, the rules of the game are displayed. 

![rules of the game](docs/images/rules.jpg)

The user presses enter to continue to the game. 

### User selects 2

When the user selects choice 2, the game begins. The user is shown the 'secret' word by the computer and is prompeted to guess their letter:

![guess the letter](docs/images/guess_letter.jpg)

### User chooses an incorrect letter

If the user selects an incorrect letter, their tries are reduced by 1, the hangman graphic draws one stage and the letter they have tried is added to the letters used array:

![play the game](docs/images/gameplay.jpg)

### User chooses a correct letter

when the user chooses a correct letter, that letter appears in it's place in the word. 
Correct uppercase letters render where they appear in the word, for example, if the user selects the letter 'b' and the secret workd is 'Batman', the letter 'b' will appear in uppercase. 

## ***Errors and notifications***

### Errors
Only alphabetic characters are permitted. If the user enters numeric or special characters, they will be informed of the error:

![non-alpha character](docs/images/incorrect_character.jpg)

### Notifications

When the user is successful, they are notified that they have won and can play again:

![player has won](docs/images/won.jpg)

When the user has not guessed all letters correctly, they will have lost and can play again:

![player has lost](docs/images/lost.jpg)

# **Data Model**
## **Object Oriented Programming using Classes**

At the start of this project, anticipating that it would not be very extensive, I used a functional approach, creating functions in run.py. It quickly became apparent that the file was becoming large and unwieldy and difficult to read. Therefore I felt it would be beneficial to introduce a separation of concerns. 

Using Object Oriented Programming, I created 3 classes. These are 
* game - this manages the landing page and the rules
* hangman - this controls the gameplay functionality
* word - this manages the random selection of the word, prints the word/shows an underscore, checks if the letter is in the word etc. 

# ***Libraries***
This project did not require any external libraries and used build in Python library/module random found at 

https://docs.python.org/3/library/random.html

The purpose of this for this project was to randomly choose the word for the game from game_data.py using the random.choice function. 

# ***Other separation of concerns***

The game data, i.e. the lists of 'secret' words and the hangman stages graphics, were quite long and took up a lot of space. As such, these were moved to their own file, game_data.py. 
 

# **Testing**
This project was tested iteratively throughout the build in the following ways. 

* Testing the code in small chunks in the VS terminal to ensure that it was working as expected
* Testing the game once deployed to Heroku and in subsequent deployments by playing it using the different functionality to test expected outcomes. 
* Testing the user inputs thoroughly. Negative testing to ensure errors and notifications work as expected. 

***PEP8 testing***
I checked the code in the PEP8 vaildator. The following errors were returned


* word.py - corrected trailing white space. 
* run.py - no errors
* hangman.py 
  - Error: Line 29, line too long
  - Fix: did not amend as code read poorly broken over 2 lines and game not affected
* game_data.py 
  - Error: blank line at end of file
  - Fix: deleted blank line



## ***Deployment to Heroku*** 
The following are the steps taken to deploy to Heroku. 

* Create an account in Heroku. 
* Click on the 'New' button.
* In the Heroku dashboard, click 'Create new app'
* Then, create a unique name for the app
* Select your region, Europe/USA
* Click 'Create app'
* Navigate to 'Settings' from the settings tab. 
* Click the button labelled "Reveal Config Vars" and enter PORT for the key and 8000 as the Value and click the "add" button.
* The next step will add buildpacks to the application. 
* Click 'Add Buildpacks' and select Python and 'Save changes'
* Add another build pack called node.js to handle the mock terminal code and click 'Save' again
* Next navigate to the Deploy section from the deploy tab
* In the Deployment Method section, select GitHub
* Search for the GitHub repository name and click 'connect' when it has been correcly identified
* Select the correct branch to deploy from, in this case 'main' and select 'Automatic deploys'
* Click the 'View' button to navigate to the deployed link


## ***Credits**

[make all letters used lowercase](https://www.delftstack.com/howto/python/python-lowercase-list/)

[remove all white spaces in word split and set to lower case](https://www.programiz.com/python-programming/methods/built-in/filter)

[list contains elements](https://www.techbeamers.com/program-python-list-contains-elements/)
[also:list contains elements](https://www.programiz.com/python-programming/methods/built-in/all)

[limit inpu string character length](https://stackoverflow.com/questions/8761778/limiting-python-input-strings-to-certain-characters-and-lengths)

[OOP tutorial](https://realpython.com/python3-object-oriented-programming/)

Some initial inspiration videos/documentation
[Hangman video](https://www.youtube.com/watch?v=m4nEnsavl6w)
[sample code]()

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