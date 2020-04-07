#!/bin/bash
# Sends a JSON POST req to URL as 1st arg and displays the body response
curl -s POST -H "Content-Type: application/json" -d @"$2" "$1"
