#!/usr/bin/python3
"""
Write a function that returns True if the object
is an instance of a class that inherited
(directly or indirectly) from the specified
class ; otherwise False.
"""


def inherits_from(object, theClass):
    """
    returns True if the object is an instance of
    a class that inherited (directly or indirectly)
    from the specified class ; otherwise False
    """
    return issubclass(type(object), theClass) and type(object) is not theClass
