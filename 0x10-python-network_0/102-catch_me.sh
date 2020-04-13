#!/bin/bash
# Script req to 0.0.0.0:5000/catch_me causing the server to respond w/a message
curl --silent --location --header "Origin: HolbertonSchool" -X PUT --data "user_id=98" 0.0.0.0:5000/catch_me
