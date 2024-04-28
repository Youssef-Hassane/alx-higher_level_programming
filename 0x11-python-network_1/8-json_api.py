#!/usr/bin/python3
"""
A script that takes in a letter, sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter,
and prints the result.
"""
import sys
import requests


if __name__ == "__main__":
    # Get letter from command line arguments, default to empty string
    search_letter = sys.argv[1] if len(sys.argv) > 1 else ""

    # Create payload with letter
    payload = {"q": search_letter}

    # Send POST request to http://0.0.0.0:5000/search_user
    response = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        # Parse JSON response
        data = response.json()

        # Print result if there is one, else print "No result"
        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
    except ValueError:
        print("Not a valid JSON")
