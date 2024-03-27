#!/bin/bash
# This script takes a URL as input, sends a request to that URL using curl, and displays th# e size of the body of the response in bytes

curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
