#!/usr/bin/python3
def roman_to_int(roman_string):
    # If the input is not a string, return 0
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    # Define the Roman numerals and their integer values
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    # Initialize the integer value and previous value
    integer_value = 0
    # Iterate through the Roman numeral string in reverse
    prev_value = 0
    # Loop through each numeral in the string
    for numeral in reversed(roman_string):
        # Get the integer value of the numeral
        value = roman_numerals[numeral]
        # Check if the value is less than the previous value
        if value < prev_value:
            # Subtract the value from the integer value
            integer_value -= value
        else:
            # Add the value to the integer value
            integer_value += value
        # Update the previous value
        prev_value = value
    # Return the integer value
    return integer_value
