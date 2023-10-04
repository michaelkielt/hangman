import random

# Creating a class for the hangman game
class Hangman:
    # Creating init function for all the attributes of the class
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []


    def _print_game_standing(self, user_guess):
        if user_guess in self.word:
            print("Good guess! '{}' is in the word.".format(user_guess))
        else: 
            print("Sorry, '{}' is not in the word. Try again.".format(user_guess))
            self.num_lives -= 1
            print("You have '{}' number of lives left".format(self.num_lives))

    def _update_guessed_word(self, user_guess):
        for i, letter in enumerate(self.word):
            if letter == user_guess:
                self.word_guessed[i] = user_guess
        self.num_letters -= 1

    def _ask_for_input(self):
        while True:
            user_guess = input("Please guess by entering a letter").lower()
            if len(user_guess) != 1 or not user_guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif user_guess in self.list_of_guesses:
                print("You already tried that letter!")
            elif len(user_guess) == 1 and user_guess.isalpha() and user_guess not in self.list_of_guesses:
                self._print_game_standing(user_guess)
                self._update_guessed_word(user_guess)
                self.list_of_guesses.append(user_guess)
                break

word_list = ["Strawberry", "Mango", "Pineapple", "Kiwi", "Nectarine"]
hangman_game = Hangman(word_list)
hangman_game._ask_for_input()