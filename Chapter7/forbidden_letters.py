# Date: 06/05/2025
# Program to implement the use_none function that checks if a word contains any forbidden letters

def uses_none(word, forbidden):
    """ Checks whether a word avoids forbidden letters.

    Args:
        word: string to check
        forbidden: string of letters that should not appear in word
    
    Returns:
        True if word contains none of the forbidden letters, False otherwise

    >>> uses_none("banana", "xyz")
    True
    >>> uses_none("apple", "efg")
    False
    >>> uses_none("hello", "aeiou")
    False
    >>> uses_none("rythm", "aeiou")
    True
    >>> uses_none("", "xyz")
    True
    >>> uses_none("python", "")
    True
    """

    # Check each forbidden letter
    for letter in forbidden:
        # If any forbidden letter is in the word, return False
        if letter in word:
            return False
    # If we get here, no forbidden letters were found
    return True

# Run the doctests
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Additional test cases
    print("Testing uses_none function:")
    test_cases = [
            ("banana", "xyz"),
            ("apple", "efg"),
            ("hello", "aeiou"),
            ("rhythm", "aeiou"),
            ("", "xyz"),
            ("python", "")
        ]

    for word, forbidden in test_cases:
        result = uses_none(word, forbidden)
        print(f"Word: '{word}', Forbidden: '{forbidden}' -> {result}")
