#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    allNames = dir(hidden_4)
    sortedNames = sorted(filter(lambda x: not x.startswith("__"), allNames))

    for eachName in sortedNames:
        print(eachName)
