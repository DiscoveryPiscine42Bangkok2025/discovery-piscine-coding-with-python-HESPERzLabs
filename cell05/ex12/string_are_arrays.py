#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) != 1:
    print("none")
else:
    text = args[0]
    found = ""

    for char in text:
        if char == "z":
            found += "z"

    if found:
        print(found)
    else:
        print("none")
