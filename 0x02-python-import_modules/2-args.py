#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    numberOfArguments = len(argv) - 1

    if numberOfArguments == 0:
        print("0 arguments.")
    else:
        print("{:d} argument{}:".format(
            numberOfArguments, 's' if numberOfArguments > 1 else ''))
        for index in range(1, numberOfArguments + 1):
            print("{:d}: {}".format(index, argv[index]))
