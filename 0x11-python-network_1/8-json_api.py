#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
from sys import argv


if __name__ == "__main__":
    dic = {'q': ""}

    if len(argv) > 1:
        dic['q'] = argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', dic)

    if 'json' not in r.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        if r.json():
            print('[{}] {}'.format(r.json().get('id'), r.json().get('name')))
        else:
            print("No result")
