#!/usr/bin/python3
""" Defines a text-indentation function """


def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): Input text.

    Raises:
        TypeError: If text is not a string.

    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Iterate through each character in the text
    for character in ".?:":
        # Split the text into lines
        text = (character + "\n\n").join(
            [line.strip(" ") for line in text.split(character)])
    # Print the text with 2 new lines after each of these characters
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
