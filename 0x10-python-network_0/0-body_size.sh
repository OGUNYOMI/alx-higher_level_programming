#!/bin/bash
# This script takes a URL as input, sends a request to that URL using curl, and 
# displays the size of the body of the response in bytes

curl -sI "$1" | awk '/Content-Length/ {print $2}'
