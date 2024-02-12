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
    def to_json_string(dict_list):
        """Convert a list of dictionaries to a JSON string.

        Args:
            dict_list (list): A list of dictionaries to be
            converted to JSON string.

        Returns:
            str: The JSON string representation of dict_list.
            Returns an empty list
            as a JSON string if dict_list is None or empty.
        """
        if not dict_list:
            return "[]"
        return json.dumps(dict_list)

    @classmethod
    def save_to_file(cls, objects):
        """Save the JSON string representation of a list of objects to a file.

        The file is named after the class of the objects.

        Args:
            objects (list): A list of instances that inherit from Base.

        Side Effects:
            Writes the JSON string to a file with the name <ClassName>.json.
            If the list is None or empty, writes an empty list to the file.
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w') as file:
            if objects is None:
                file.write("[]")
            else:
                object_dicts = [obj.to_dictionary() for obj in objects]
                file.write(Base.to_json_string(object_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Convert a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string representation of a list of
            dictionaries.

        Returns:
            list: A list of dictionaries represented by json_string.
            Returns an empty list if json_string is None or empty.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **attributes):
        """Instantiate an object from attribute dictionary.

        This method creates a new instance of the class upon which it's called
        (either Rectangle or Square) using a set of predefined initial values.
        The instance is then updated with the given attributes.

        Args:
            **attributes: Arbitrary keyword arguments containing attributes
            for the instance.

        Returns:
            The new, updated instance of the class.
        """
        from models.rectangle import Rectangle
        from models.square import Square

        # Determine the class type and create a
        # new instance with default values.
        if cls is Rectangle:
            # Default width and height for Rectangle.
            instance = Rectangle(1, 1)
        elif cls is Square:
            instance = Square(1)  # Default size for Square.
        else:
            instance = None  # In case cls is neither Rectangle nor Square.

        # Update instance with the provided attributes and return it.
        instance.update(**attributes)
        return instance
