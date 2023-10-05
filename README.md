# Hangman Game

## Table of Contents
- [Description](#description)
- [Installation](#installation)

## Description

The Hangman Game is a classic word-guessing game  in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts, one letter at a time. This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. The game aims to provide an enjoyable and interactive experience for players while demonstrating the use of various data structures such as lists and conditional statements like if-else blocks and while loops in a Python program.

### Project Goals and Learning Objectives

The primary goals of this project are as follows:

- Develop a functioning Hangman game that allows players to:
  - Guess letters to complete the hidden word.
  - Track their progress and remaining guesses.
  - Win by correctly guessing the word or lose by running out of guesses.
- Implement different data structures, including lists to store words, letters, and conditional statements like if-else blocks and while loops for game logic.
- Enhance problem-solving skills by creating algorithms for word selection, word masking, and player-input validation.


### What I Learned

Throughout the development of this Hangman game project, I learned and developed several key concepts and skills:

1. Python Programming: I developed my Python programming skills, utilising fundamental concepts like variables, data structures like lists and strings, conditional statements, and loops to build a fully functional game.
2. Problem-Solving: I implemented algorithms for critical game components such as word selection, input validation and checking player guesses. This experience enhanced my problem-solving capabilities and developed my algorithm skills in Python.
3. User Input Handling: I gained valuable experience in handling user input effectively.
4. Game Logic: I constructed the game's logic to manage the game's status, monitor player progress in the form of player lives, and track remaining guesses.
5. Code Organisation and Readability: I improved the overall quality of my code by incrementally refactoring and optimising at several stages, as well as testing thoroughly to ensure each component was working as expected. I also tried to implement the Single Responsibility Principle to the best of my ability when breaking down my functions into smaller, more focused ones.

### Installation

To install the Hangman game, please follow these instructions: 

1. Clone the repository to your local computer using Git:

   ```bash
   https://github.com/michaelkielt/hangman.git
   ```

2. Navigate to the project directory:

   ```bash
   cd hangman
   cd hangman-game
   ```

3. Run the game by executing the Python script:

   ```bash
   python hangman-play.py
   ```

4. The game will start, and you can begin playing by entering your guesses.


### Usage Instructions

Once you've started the game, you can play Hangman by following these simple instructions:

1. The game randomly selects a secret word from the predefined list.

2. You'll be presented with a masked version of the word, represented by underscores for unguessed letters.

3. Enter a single letter as your guess and press Enter.

4. The game will check your guess and inform you whether your guess is correct.

5. Continue guessing one letter at a time until you guess the entire word (win-scenario) or run out of lives (lose-scenario).

6. The game will let you know if you've won or lost with a printed message.


### File Structure

This is how I structured my files for this project:

```
hangman-game/
│
├── hangman-play.py             # Main Python script for the Hangman game
│
├── README.md              # Documentation and instructions
│
└── .gitignore             # Gitignore file to specify which files to exclude from version control
```


### License information

This Hangman game project is licensed under the MIT License. You are free to use, modify, and distribute this project for personal or educational purposes. Please refer to the LICENSE.md file for the full license details.
