#!/usr/bin/python3
""" LockedClass only allows attribute 'first_name' to be set """


class LockedClass:
    """
    LockedClass only allows attribute 'first_name' to be set.
    Any other attribute assignments will raise an AttributeError.
    """
    __slots__ = ['first_name']
