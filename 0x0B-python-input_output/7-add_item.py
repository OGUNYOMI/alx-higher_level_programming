#!/usr/bin/python3
import json
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


def add_arguments_to_list(arguments):
    try:
        data = load_from_json_file("add_item.json")
    except FileNotFoundError:
        data = []

    data.extend(arguments)
    save_to_json_file(data, "add_item.json")


if __name__ == "__main__":
    add_arguments_to_list(sys.argv[1:])
