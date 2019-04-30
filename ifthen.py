#!/usr/bin/env python3

# Learning about if/then statements

if 1 == 1 and 5 == 4:
    print("That is true")

else:
    print("That is false")

if 1 == 1 and 5 >= 4:
    print("That is true")
    if 27 < 30 and 27 > 20:
        print("27 is between 20 and 30")

else:
    print("That is false")

ages = [27, 35, 42]

if ages[0] > 30 and ages[0] < 70:
    print("You are a worker")

else:
    print("Millenial")

if ages[1] > 30 and ages[1] < 70:
    print("You are a worker")

else:
    print("Millenial")

if ages[2] > 30 and ages[2] < 70:
    print("You are a worker")

else:
    print("Millenial")
