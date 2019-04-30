#!/usr/bin/env python3
message = 'You have received a(n) '
print('What is your numerical score?')
connection = int(input())
if connection in range(0, 59):
    message = message + 'F.'
elif connection in range(60, 69):
    message = message + 'D.'
elif connection in range(70, 79):
    message = message + 'C.'
elif connection in range(80, 89):
    message = message + 'B.'
else:
    message = message + 'A.'
print(message)
