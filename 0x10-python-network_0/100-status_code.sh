#!/bin/bash
# Sends a request to URL passes as arg and displays the status code
curl -s -o /dev/null --head --write-out "%{http_code}" "$1"
