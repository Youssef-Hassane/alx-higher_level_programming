#!/usr/bin/python3

for theNumber in range(100):
    print("{:02d}".format(theNumber), end=(", " if theNumber < 99 else "\n"))
