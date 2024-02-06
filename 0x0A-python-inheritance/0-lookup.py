#!/usr/bin/python3
"""
Function that returns the list
of available attributes and
methods of an object
"""


def lookup(object):
    """Return a list of available attributes and methods of an object."""
    return dir(object)
