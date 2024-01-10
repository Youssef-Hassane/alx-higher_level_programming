#!/usr/bin/python3
def common_elements(firstSet, secondSet):
    # First Set: { "Python", "C", "Javascript" }
    # Seond Set: { "Bash", "C", "Ruby", "Perl" }
    intersection_set = firstSet & secondSet
    # intersection_set = "C"
    return intersection_set

# Alternative way to do it:
# def common_elements(set_1, set_2):
#     return set_1.intersection(set_2)
