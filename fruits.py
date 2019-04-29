#!/usr/bin/env python3

fruits = ['blueberry', 'blackberry', 'raspberry']

join_method = ":".join(fruits)

print(join_method)

print("I like " + fruits[0] + ", " + fruits[1] + " and " + fruits[2], 2)

print("I don't like {0}. I do like {1}. I love {1}. I am {0} years old".format(42, fruits[2]))

print(f"I am eating a {fruits[1]}")
