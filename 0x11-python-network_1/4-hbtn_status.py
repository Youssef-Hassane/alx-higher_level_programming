#!/usr/bin/python3
"""
Fetches and prints the body response of the HTTP GET request to
https://intranet.hbtn.io/status.
"""
import requests


if __name__ == "__main__":
    # Send a GET request to the URL and store
    # the response in the variable `response`
    with requests.get("https://alx-intranet.hbtn.io/status") as res:
        r = res.text
        # Print the body response of the `response`
        print("Body response:")
        # Print the type of the response text
        print(f"\t- type: {type(r)}")
        # Print the content of the response text
        print(f"\t- content: {r}")
