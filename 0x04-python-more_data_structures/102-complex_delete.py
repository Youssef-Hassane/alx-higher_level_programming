#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    # Create a new dictionary
    new_dict = {}
    # Iterate through the original dictionary and add 
    # key-value pairs that don't match the specified value
    for key, val in a_dictionary.items():
        # Check if the value matches the specified value
        if val != value:
            # Add the key-value pair to the new dictionary
            new_dict[key] = val
    # Return the new dictionary
    return new_dict
