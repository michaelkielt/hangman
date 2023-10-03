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