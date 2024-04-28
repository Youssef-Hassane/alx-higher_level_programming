#!/usr/bin/python3
"""
A script that retrieves the X-Request-Id header from a URL.

Usage:
    python 6-post_email.py <url>
"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    with requests.post(sys.argv[1], data=values) as res:
        print(res.text)
