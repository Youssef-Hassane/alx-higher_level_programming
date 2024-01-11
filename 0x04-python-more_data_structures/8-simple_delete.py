#!/usr/bin/python3
def simple_delete(theDictionary, theKey=""):
    # Delete a key-value pair from a dictionary
    if theKey in theDictionary:
        # Use the del keyword to delete the key-value pair
        del theDictionary[theKey]
    # Return the updated dictionary
    return theDictionary
