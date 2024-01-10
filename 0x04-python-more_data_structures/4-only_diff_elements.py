#!/usr/bin/python3
def only_diff_elements(firstSet, secondSet):
    # Use symmetric difference to get elements present in only one set
    diff_set = firstSet.symmetric_difference(secondSet)
    
    return diff_set
