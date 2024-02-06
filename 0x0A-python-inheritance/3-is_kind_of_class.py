#!/usr/bin/python3
"""
Write a function that returns True if the object
is an instance of, or if the object is an
instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(object, theClass):
    """
    the is_kind_of_class function
    """
    return isinstance(object, theClass)
