#!/usr/bin/python3

for character in range(ord('a'), ord('z') + 1):
    if chr(character) not in ['q', 'e']:
        print("{}".format(chr(character)), end="")
