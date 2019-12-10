#!/usr/bin/python3
def uppercase(str):
    s = 0
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            s = 32
        else:
            s = 0
        print("{:c}".format(ord(letter) - s), end="")
    print()
