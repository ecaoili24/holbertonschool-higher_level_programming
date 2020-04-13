#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""

import urllib.request
req = urllib.request.Request('https://intranet.hbtn.iostatus')
with urllib.request.urlopen(req) as response:
        page = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(page)))
        print('\t- content: {}'.format(page))
        print('\t- utf8 content: {}'.format(page.decode('UTF-8')))
