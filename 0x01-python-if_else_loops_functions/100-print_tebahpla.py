#!/usr/bin/python3
for letter in range(ord('z'), ord('a') - 1, -1):
    if letter % 2 is 1:
        letter = letter - ord(' ')
    print("{}".format(chr(letter)), end="")
