#!/usr/bin/python3
"""
A script that displays X-Request-Id header of a given URL.
"""

import sys
import requests


def main():
    """Main function of the program."""
    url = get_url_from_command_line()
    request_id = get_request_id_from_url(url)
    print_request_id(request_id)


def get_url_from_command_line():
    """Get URL from command line arguments."""
    return sys.argv[1]


def get_request_id_from_url(url):
    """Get request id from URL."""
    response = requests.get(url)
    return response.headers.get("X-Request-Id")


def print_request_id(request_id):
    """Print request id."""
    print(request_id)


if __name__ == "__main__":
    main()
