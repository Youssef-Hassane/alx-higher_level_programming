#!/usr/bin/python3
"""
Fetches and prints the body response of the HTTP GET request to
https://intranet.hbtn.io/status.
"""
import requests


if __name__ == "__main__":
    # Send a GET request to the URL and store
    # the response in the variable `response`
    response = requests.get("https://intranet.hbtn.io/status")

    # Print the body response of the `response`
    print("Body response:")
    # Print the type of the response text
    print("\t- type: {}".format(type(response.text)))
    # Print the content of the response text
    print("\t- content: {}".format(response.text))
