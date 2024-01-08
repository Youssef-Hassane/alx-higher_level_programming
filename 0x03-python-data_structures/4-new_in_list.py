#!/usr/bin/python3
def new_in_list(myList, index, theElement):
    if 0 <= index < len(myList):
        new_list = myList.copy()
        new_list[index] = theElement
        return new_list
    else:
        return myList
