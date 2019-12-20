#!/usr/bin/python3
def complex_delete(a_dictionary, val):
    for key in list(a_dictionary):
        if a_dictionary[key] == val:
            del a_dictionary[key]
    return a_dictionary
