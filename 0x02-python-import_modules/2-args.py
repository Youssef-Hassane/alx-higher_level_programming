#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    count = len(sys.argv)
    if count == 1:
        print("0 arguments.")
    elif count == 2:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(count - 1))
    for i in range(count - 1):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
