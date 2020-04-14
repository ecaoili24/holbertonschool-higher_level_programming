#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    req = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        val = req.json()
        if val == {}:
            print("No result")
        else:
            print("[{}] {}".format(val.get("id"), val.get("name")))
    except ValueError:
        print("Not a valid JSON")
