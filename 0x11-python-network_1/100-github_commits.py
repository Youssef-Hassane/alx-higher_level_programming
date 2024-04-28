#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.
"""

import sys
import requests


# Main function of the program
if __name__ == "__main__":
    # Get GitHub credentials from command line arguments
    owner: str = sys.argv[1]  # Owner of the repository
    repository: str = sys.argv[2]  # Name of the repository

    # Create URL for request
    url: str = "https://api.github.com/repos/{}/{}/commits"\
        .format(owner, repository)

    # Send GET request to GitHub API to retrieve commits
    response: requests.Response = requests.get(url)

    # Parse JSON response
    commits: list = response.json()

    # Print the 10 most recent commits
    for i in range(min(len(commits), 10)):
        sha: str = commits[i].get("sha")  # Get commit SHA
        # Get author name
        author_name: str = commits[i].get("commit").get("author").get("name")
        print("{}: {}".format(sha, author_name))  # Print commit info
