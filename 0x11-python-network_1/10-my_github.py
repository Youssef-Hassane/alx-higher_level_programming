#!/usr/bin/python3
"""
A script that displays a GitHub user's id using their credentials.
"""

# Import necessary modules
import sys  # Used for command line arguments
import requests  # Used to interact with the GitHub API
from requests.auth import HTTPBasicAuth  # Used to authenticate with GitHub API


# Main function of the program
if __name__ == "__main__":
    # Get GitHub credentials from command line arguments
    username: str = sys.argv[1]
    password: str = sys.argv[2]

    # Create HTTPBasicAuth object for authentication
    auth: HTTPBasicAuth = HTTPBasicAuth(username, password)

    # Send GET request to GitHub API to retrieve user's id
    response: requests.Response = requests.get(
        "https://api.github.com/user", auth=auth)

    # Print user's id
    print(response.json().get("id"))
