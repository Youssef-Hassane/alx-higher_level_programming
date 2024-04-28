#!/usr/bin/python3
"""
Script that fetches URL and prints its body using urllib package.
"""


if __name__ == '__main__':
    import urllib.request

    # Define URL to fetch
    url = 'https://alx-intranet.hbtn.io/status'

    # Open URL and read content
    with urllib.request.urlopen(url) as response:
        content = response.read()

        # Print body response
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
