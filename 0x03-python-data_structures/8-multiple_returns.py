#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (0, None)

    theLength = len(sentence)
    firstCharacter = sentence[0]
    return (theLength, firstCharacter)
