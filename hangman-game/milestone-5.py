import random


class Hangman:
    """
    A Hangman Game that allows the player to guess letters in a secret word. The game initializes with a list of
    words and the option to specify the number of lives.

    Args:
        word_list (list): A list of words from which the secret word is randomly selected.
        num_lives (int, optional): The number of lives the player starts with (default is 5).
    
    Attributes:
        word (str): The secret word to be guessed.
        word_guessed (list): A list representing the letters of the word, with '_' for unguessed letters.
        num_letters (int): The count of unique letters in the word yet to be guessed.
        num_lives (int): The current number of lives the player has.
        list_of_guesses (list): A list of letters that the player has guessed.

    Methods:
        _print_game_standing(user_guess):
            Checks if a letter is in the secret word.
        _update_guessed_word(user_guess):
            Updates the word_guessed representation with the correct guess.
        _ask_for_input(user_guess):
            Prompts the user for a letter guess until valid input is provided.            
    
    """    

    def __init__(self, word_list, num_lives=5):
        """
        Initialize the Hangman game with a list of words and the number of lives.

        Args:
            word_list (list): A list of words from which the secret word is randomly selected.
            num_lives (int): The number of lives the player starts with. Default is 5.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

        print(f"The mystery word has '{self.num_letters}' characters in it!")
        print(f"{self.word_guessed}")

        """
        Prints the current game standing after checking if the user's guess is in the
        secret word.

        Args:
            user_guess (str): The letter guessed by the user taken from the input function.
        """
    def _print_game_standing(self, user_guess):
        if user_guess in self.word:
            print(f"Good guess! {user_guess} is in the word.")
        else: 
            print(f"Sorry, {user_guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} number of lives left")
       
        """
        Updates the word_guessed representation with the correct guess.

        Args:
            user_guess (str): The letter guessed by the user.
        """
    def _update_guessed_word(self, user_guess):
        for i, letter in enumerate(self.word):
            if letter == user_guess:
                self.word_guessed[i] = user_guess
        self.num_letters -= 1
       
        """
        Continuously prompt the user to guess a letter until a valid input is provided.
        """
    def _ask_for_input(self):
        while True:
            user_guess = input("Please guess by entering a letter")
            user_guess = user_guess.lower()
            if len(user_guess) != 1 or not user_guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif user_guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self._print_game_standing(user_guess)
                self._update_guessed_word(user_guess)
                self.list_of_guesses.append(user_guess)
                break


def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        if game.num_letters > 0:
            game._ask_for_input()
        if game.num_lives > 0 and not game.num_letters > 0:
            print("Congratulations, you won the game!")
            break   

if __name__ == '__main__':
    word_list = ["strawberry", "mango", "pineapple", "kiwi", "nectarine"]
    play_game(word_list)


