#!/usr/bin/python3
"""Module 9-add_item
Adds all arguments to a Python list, and then save them to a file
"""


import sys
import json


save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

filename = "add_item.json"
my_list = []
try:
    my_list = load_from_json_file(filename)
except:
    my_list = []
for x in range(1, len(sys.argv)):
    my_list.append(sys.argv[x])
save_to_json_file(my_list, filename)
