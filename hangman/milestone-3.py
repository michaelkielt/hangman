# Creating a while loop that will ask the user for guesses and validate them
# Setting the condition to 'True' so that the loop will continuously run

while (True):
    guess = input("Please guess by entering a letter")

    # Check if the guess is a single letter and alphabetical
    # If the guess is valid the loop breaks
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")

secret_word = "apple"

# Checking if the guessed letter is in the secret word
if guess in secret_word:
    print("Good guess! '{guess}' is in the word.")
else:
    print("Sorry, '{guess}' is not in the word. Try again.")    