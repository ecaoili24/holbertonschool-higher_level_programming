#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        max_number = my_list[0]
        for x in my_list[1:]:
            if max_number < x:
                max_number = x
        return max_number
    return None
