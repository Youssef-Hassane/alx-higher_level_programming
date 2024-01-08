#!/usr/bin/python3
def no_c(myString):
    theResult = ""
    for Character in myString:
        if Character not in "cC":
            theResult += Character
    return theResult
