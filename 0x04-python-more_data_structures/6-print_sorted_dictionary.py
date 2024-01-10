#!/usr/bin/python3
# Write a function that prints a dictionary by ordered keys.
def print_sorted_dictionary(theDictionary):
    # Use the sorted() function to get a sorted list of keys
    for key in sorted(theDictionary):
        # Print each key-value pair
        print("{}: {}".format(key, theDictionary[key]))
