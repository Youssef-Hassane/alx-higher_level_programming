#!/usr/bin/python3
"""
A script that sends a POST request to a URL with an email parameter,
and displays the response body.

@author Tristan Zippers
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    # Assign command line arguments to variables
    url = sys.argv[1]  # URL to send request to
    email_param = {"email": sys.argv[2]}  # Email parameter

    # Encode email parameter and convert to bytes
    data = urllib.parse.urlencode(email_param).encode("ascii")

    # Create request object with URL and data
    request = urllib.request.Request(url, data)

    # Open URL and print response body
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
