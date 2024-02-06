#!/usr/bin/python3
"""
Write a function that adds a new
attribute to an object if it’s possible:
"""


def add_attribute(obj, attribute, value):
    """Add a new attribute to an object if possible """

    if hasattr(obj, '__dict__') or isinstance(obj, type):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
