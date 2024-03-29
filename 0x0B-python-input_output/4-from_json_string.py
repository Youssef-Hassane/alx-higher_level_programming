#!/usr/bin/python3
"""
Write a function that returns an object
(Python data structure) represented by a JSON string:
Prototype: def from_json_string(my_str):
You don’t need to manage exceptions if
the JSON string doesn’t represent an object.
"""
import json


def from_json_string(json_string):
    """
    Converts a JSON string into a corresponding Python object.
    """
    return json.loads(json_string)
