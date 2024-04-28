#!/usr/bin/python3
"""Script that displays X-Request-Id header of a given URL.
"""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.headers["X-Request-Id"])
