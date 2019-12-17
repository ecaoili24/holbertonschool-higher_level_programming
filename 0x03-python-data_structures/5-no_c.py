#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for c in my_string:
        if c == 'c' or c == 'C':
            continue
        else:
            string = string + c
    return string
