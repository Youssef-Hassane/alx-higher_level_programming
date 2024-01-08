#!/usr/bin/python3
def delete_at(myList=[], index=0):
    if index >= len(myList) or index < 0:
        return myList
    del myList[index]
    return myList
