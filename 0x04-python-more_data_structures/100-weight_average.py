#!/usr/bin/python3
def weight_average(my_list=[]):
    # Return 0 if the list is empty
    if not my_list:
        return 0
    # Calculate the weighted average
    total_score = 0
    total_weight = 0
    # Iterate through the list and calculate the weighted average
    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    # Return the weighted average
    return total_score / total_weight
