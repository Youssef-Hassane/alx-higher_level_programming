#!/usr/bin/python3
"""Script that displays X-Request-Id header of a given URL.
"""
import sys
import urllib.request

if __name__ == "__main__":
    # Get URL from command line argument
    url = sys.argv[1]

    # Create request object
    request = urllib.request.Request(url)

    # Open URL and print X-Request-Id header
    with urllib.request.urlopen(request) as response:
        header_dict = dict(response.headers)
        request_id = header_dict.get("X-Request-Id")
        print("X-Request-Id:", request_id)
