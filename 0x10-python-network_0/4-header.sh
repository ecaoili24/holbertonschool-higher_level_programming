#!/bin/bash
# Script that takes in URL as arg, sends GET req to it, + displays body
curl -s GET -H "X-HolbertonSchool-User-Id: 98" "$1"
