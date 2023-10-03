# Creating a while loop that will ask the user for guesses and validate them
# Setting the condition to 'True' so that the loop will continuously run

secret_word = "apple"

while (True):
    guess = input("Please guess by entering a letter")

    # Check if the guess is a single letter and alphabetical
    # If the guess is valid the loop breaks
    if len(guess) == 1 and guess.isalpha():
        # Checking if the guessed letter is in the secret word
        if guess in secret_word:
            print(f"Good guess! '{guess}' is in the word.")    
            break
        else:
            print(f"Sorry, '{guess}' is not in the word. Try again.")
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")


       
    