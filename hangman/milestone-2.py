# -*- coding: utf-8 -*-
import random

# Creating a list of my 5 favourite fruits
word_list = ["Strawberry", "Mango", "Pineapple", "Kiwi", "Nectarine"]


# Selecting a random item from the list and assigning it to the 'word' variable
word = random.choice(word_list) 
print(word)

# Getting input from the user and assigning it to a variable named 'guess'
guess = input("Please enter a single letter...")

# Validating that the guess is the correct length and alphabectical
if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("Oops! That is not a valid input")