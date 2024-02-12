#!/usr/bin/python3
"""
The module contains the class Base
"""
import json

class Base:
    """ Base class """
    # private class attribute called __nb_objects
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes the base class """
        # 1 - If id is not None, assign the public instance attribute id
        # with this argument value - you can assume id is an integer
        # and you don’t need to test the type of it
        if id is not None:
            self.id = id
        # Otherwise, increment __nb_objects and assign the new
        # value to the public instance attribute id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Return the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)


