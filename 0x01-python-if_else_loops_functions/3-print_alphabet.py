#!/usr/bin/python3
for LOWERCASE_letter in range(ord('a'), ord('z') + 1):
    if LOWERCASE_letter != ord('e') and LOWERCASE_letter != ord('q'):
        print("{:c}".format(LOWERCASE_letter), end="")
