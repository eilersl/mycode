#!/usr/bin/env python3

"""
Author: LEilers

This program asks a silly question
"""

ROUND = 0
while True:
    ROUND = ROUND + 1
    print("Finish the movie title, 'Monty Python\'s The Life of _____'")
    ANSWER = input()
    if ANSWER.lower() == "brian":
        print("Correct")
        break
    elif ANSWER.lower() == "shrubbery":
        print("You gave the super secret answer!")
        break
    elif ROUND == 3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try again!")
