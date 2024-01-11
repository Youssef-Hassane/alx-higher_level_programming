#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Create a new dictionary
    new_dict = {}
    # Iterate through the original dictionary and multiply each value by 2
    for key, value in a_dictionary.items():
        new_dict[key] = value * 2
    # Return the new dictionary
    return new_dict
