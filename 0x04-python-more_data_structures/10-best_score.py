#!/usr/bin/python3
def best_score(a_dictionary):
    # If the dictionary is empty, return None
    if not a_dictionary:
        return None
    # Return the key with the biggest integer value
    return max(a_dictionary, key=a_dictionary.get)
