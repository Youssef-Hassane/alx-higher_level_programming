#!/usr/bin/python3
"""
A script that retrieves the X-Request-Id header from a URL.

Usage:
    python 6-post_email.py <url>
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
        # Print X-Request-Id header
        header_dict = dict(response.headers)
        request_id = header_dict.get("X-Request-Id")
        print("X-Request-Id:", request_id)
