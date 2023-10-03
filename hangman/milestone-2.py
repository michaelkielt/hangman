# -*- coding: utf-8 -*-
import random

# Creating a list of my 5 favourite fruits
favourite_fruits = ["Strawberry", "Mango", "Pineapple", "Kiwi", "Nectarine"]
for fruit in favourite_fruits:
    print(fruit)

# Selecting a random item from the favourite_fruits list and assigning it to the 'random_fruit' variable
random_fruit = random.choice(favourite_fruits) 
print(random_fruit)

# Getting input from the user and assigning it to a variable named 'guess'
guess = input("Please enter a single letter...")

# Validating that the guess is the correct length and alphabectical
if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("Oops! That is not a valid input")