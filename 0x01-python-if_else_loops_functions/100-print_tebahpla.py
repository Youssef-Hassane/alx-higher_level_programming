#!/usr/bin/python3

for index in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(index - (32 if index % 2 != 0 else 0)), end="")
