#!/usr/bin/python3
def uniq_add(my_list=[]):
    return sum(set(my_list))

# Another solution:
# def uniq_add(my_list=[]):
#     # Use a set to store unique integers
#     unique_set = set()
#     # Iterate through the list and add unique integers to the set
#     for num in my_list:
#         unique_set.add(num)
#     # Calculate the sum of unique integers
#     result = sum(unique_set)
#     # Return the result
#     return result
