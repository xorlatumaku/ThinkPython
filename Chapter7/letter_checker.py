# Date: 06/06/2025
# Program to implement the uses_only function that checks if a word contains only letters from an allowed set.

def uses_only(word, available):
    """ Checks whether a word uses only the available letters.

    Args:
        word: string to check 
        available: string of allowed letters

    Returns:
        True if word contains only letters from available, False otherwise

    >>> uses_only('banana', 'ban')
    True
    >>> uses_only('apple', 'apl')
    False
    >>> uses_only('test', 'set')
    True
    >>> uses_only('hello', 'world')
    False
    >>> uses_only('', 'abc')
    True
    >>> uses_only('aaa', 'a')
    True
    """

    # Check each letter in the word
    for letter in word:
        # If any letter is not in available letters, return False
        if letter not in available:
            return False
    # If we get here, all letters were in available
    return True

    # Run the doctests
    if __name__ == "__main__":
        import doctest
        doctest.testmod()

        # Additional test cases
        print("Testing uses_only function:")
        test_cases = [
                ('banana', 'ban'),
                ('apple', 'apl'),
                ('test', 'set'),
                ('hello', 'world'),
                ('', 'abc'),
                ('aaa', 'a')
        ]

        for word, available in test_cases:
            result = uses_only(word, available)
            print(f"Word: '{word}', Available letters: '{available}' -> {result}")
