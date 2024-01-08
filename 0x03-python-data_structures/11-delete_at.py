#!/usr/bin/python3
def delete_at(myList=[], index=0):
    if index < 0 or index >= len(myList):
        return myList

    new_list = [myList[i] for i in range(len(myList)) if i != index]
    return new_list
