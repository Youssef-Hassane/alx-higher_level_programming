#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []

    for element in my_list:
        if element == search:
            new_list += [replace]
        else:
            new_list += [element]

    return new_list
