#!/usr/bin/python3
"""
A script that takes a URL, sends a request to the URL,
and displays the body of the response.

:param url_arg: A string representing the URL to send a request to.
"""
import sys
import requests


if __name__ == "__main__":
    # Get the URL from the command line arguments
    url_arg = sys.argv[1]

    # Send a GET request to the URL and store the response in the
    # variable `response`
    response = requests.get(url_arg)

    # Print the error code if the request fails, else print the body response
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
