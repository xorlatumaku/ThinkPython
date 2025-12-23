# Date: 06/09/2025
# Program to create a more concise version of the value_counts function using the dictionary's get() method.

def value_counts(string):
    """
    Counts the occurrences of each character in a string using dict.get() method.
    Returns a dictionary with characters as keys and their counts as values.
    """
    counter = {}
    for char in string:
        # Use get() to either increment existing count or startat 0
        counter[char] = counter.get(char, 0) + 1
    return counter

def print_counts(counter, string):
    """Helper function to print the counts in a formated way."""
    print(f"\nCharacter counts for '{string}':")
    print("-" * 40)
    for char in sorted(counter.keys()):
        print(f"'{char}': {counter[char]}")
    print("-" * 40)

# Test cases
test_strings = [
        "brontosaurus",
        "programming",
        "python",
        "hello world",
        "aaaaabbcc",
        "", # empty string
        "12344321", # numbers
        "!@#$%", # special characters
    ]

# Test the function with different strings
print("Testing value_counts function:")
for test_string in test_strings:
    counter = value_counts(test_string)
    print_counts(counter, test_string)

    # Demonstrate get() method with some example lookups
    print("\nDemonstrating get() method:")
    # Test existing character
    if test_string:
        existing_char = test_string[0]
        print(f"counter.get('{existing_char}', 0) = {counter.get(existing_char, 0)}")
    # Test non-existing character
    print(f"counter.get('x', 0) = {counter.get('x', 0)}")
