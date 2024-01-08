#!/usr/bin/python3
def replace_in_list(myList, index, theElement):
    if 0 <= index < len(myList):
        myList[index] = theElement
    return myList
