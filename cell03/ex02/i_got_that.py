#!/usr/bin/env python3

msg = input("What you gotta say? : ")
if msg == "STOP":
    exit()

while True:
    msg = input("I got that! Anything else? : ")
    if msg == "STOP":
        break
