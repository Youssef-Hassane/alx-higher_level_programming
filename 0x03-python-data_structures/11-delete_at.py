#!/usr/bin/python3
def delete_at(myList=[], index=0):
    if index < 0 or index >= len(myList):
        return myList

    new_list = []
    for i, element in enumerate(myList):
        if i != index:
            new_list.append(element)

    return new_list
