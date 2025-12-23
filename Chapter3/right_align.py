# Date: 06/04/2025
# Program to print string in the 40th column of the display

def print_right(text):
    # Column width is 40
    target_column = 40

    # Calculate needed spaces
    # We need: target_column - length of text = last character postion
    spaces_needed = target_column - len(text)

    # Create the leading spaces using string repetition
    spaces = " " * spaces_needed

    # Print the spaces concatenated with the text
    print(spaces + text)

# Test the function with the given examples
print_right("Monty")
print_right("Python's")
print_right("Flying Circus")
