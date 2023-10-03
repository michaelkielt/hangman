# Hardcoding secret word for testing
secret_word = "apple"

# Creating a function for the guess checking logic
def check_guess(user_guess):
        user_guess = user_guess.lower()
        if user_guess in secret_word:
            print(f"Good guess! '{user_guess}' is in the word.")    
        else:
            print(f"Sorry, '{user_guess}' is not in the word. Try again.") 

# Creating a function for the user input validation logic
def ask_for_input():
    while (True):
        user_guess = input("Please guess by entering a letter")
        if len(user_guess) == 1 and user_guess.isalpha():
            check_guess(user_guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")


    