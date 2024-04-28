#!/usr/bin/python3
"""
A script that takes a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    # Get the URL from the command line arguments
    url = sys.argv[1]

    try:
        # Send a request to the URL and print the response decoded in utf-8
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as exception:
        # Print the error code if the request fails
        print('Error code:', exception.code)
