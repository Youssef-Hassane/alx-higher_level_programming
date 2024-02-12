#!/usr/bin/python3
"""
The module contains the class Base
"""
import json
import csv


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

    @classmethod
    def load_from_file(cls):
        """Load objects from a JSON file.

        This method loads objects from a JSON file and returns a list of
        instances of the class cls that were saved in the JSON file.

        Returns:
            list: A list of instances of the class cls that were
            saved in the JSON file.
        """
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, 'r') as file:
                object_dicts = cls.from_json_string(file.read())
            instances = [cls.create(**obj) for obj in object_dicts]
            return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, objects_list):
        """Converts the list of objects to a CSV format and saves it to a file.

        This method takes a list of objects, converts them into a CSV compatible
        format depending on their class type (Rectangle or Square), and writes
        them into a file named after the class with a '.csv' extension.
        """
        from models.rectangle import Rectangle
        from models.square import Square
        # Check if the list of objects is not empty
        if objects_list is not None:
            # Convert each object to a list depending on its type
            if cls is Rectangle:
                csv_data = [[obj.id, obj.width, obj.height, obj.x, obj.y]
                            for obj in objects_list]
            else:
                csv_data = [[obj.id, obj.size, obj.x, obj.y]
                            for obj in objects_list]
        # Open a file in write mode to save the CSV data
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(csv_data)

    @classmethod
    def load_from_file_csv(cls):
        """Loads objects from a CSV file and returns a list of instances.

        This method reads a CSV file named after the class with a '.csv'
        extension, converts the CSV data into a list of dictionaries with
        the corresponding attributes, and then uses these dictionaries to
        create and return a list of class instances.
        """
        from models.rectangle import Rectangle
        from models.square import Square
        instances_list = []
        # Open the CSV file and read the contents
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for data_row in csv_reader:
                # Convert all the string elements to integers
                data_row = [int(elem) for elem in data_row]
                # Build the dictionary with the right keys based on the class
                if cls is Rectangle:
                    attributes_dict = {"id": data_row[0], "width": data_row[1],
                                       "height": data_row[2], "x": data_row[3],
                                       "y": data_row[4]}
                else:
                    attributes_dict = {"id": data_row[0], "size": data_row[1],
                                       "x": data_row[2], "y": data_row[3]}
                # Create an instance of the class with the attributes and add it to the list
                instances_list.append(cls.create(**attributes_dict))
        return instances_list
