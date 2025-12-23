# Date: 06/06/2025
# Program to implement the New York Times Spelling Bee puzzle

def uses_only(word, available):
    """Check if word uses only available letters>"""
    for letter in word:
        if letter.upper() not in available:
            return False
    return True

def uses_all(word, required):
    """Check if word uses all required letters."""
    return required.upper() in word.upper()

def check_word(word, available, required):
    """Check whether a word is acceptable according to Spelling Bee rules.

    Args:
        word: word to check
        available: string of 7 available letters
        required: single required letter

    Returns:
        True if word is valid according to all rules, False otherwise

    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    >>> check_word('doctor', 'ACDLORT', 'R')
    True
    >>> check_word('LOAD', 'ACDLORT', 'R')
    False
    """

    # Convert word to lowercase for consistency
    word = word.lower()
    available = available.upper()
    required = required.upper()

    # Check all rules:
    # 1. Word must be at leat 4 letters long
    if len(word) < 4:
        return False

    # 2. Word must only use available letters
    if not uses_only(word, available):
        return False

    # 3. Word must use the required letter
    if not uses_all(word, required):
        return False

    return True

def word_score(word, available):
    """Compute the score for an acceptable word.

    Args:
        word: word to score (assumed to be acceptable)
        available: string of 7 available letters

    Returns:
        Score according to Spelling Bee rules

    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    >>> word_score('doctor', 'ACDLORT')
    6
    """
    # Convert everything to uppercase for comparison
    word = word.upper()
    available = available.upper()

    # Base score is word length if >= 5, or 1 if length is 4
    score = len(word) if len(word) > 4 else 1

    # Check if word is a program (uses all available letters)
    is_pangram = all(letter in word for letter in available)

    # Add 7 bonus points for pangram
    if is_pangram:
        score += 7

    return score

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Example game
    AVAILABLE = "ACDLORT"
    REQUIRED = "R"

    test_words = [
            'color', 'ratatat', 'rat', 'told', 'bee',
            'doctor', 'card', 'cartload', 'road', 'load'
    ]

    print("Spelling Bee Game")
    print(f"Available letters: {AVAILABLE}")
    print(f"Required letter: {REQUIRED}")
    print("\nTesting words:")

    total_score = 0
    for word in test_words:
        if check_word(word, AVAILABLE, REQUIRED):
            score = word_score(word, AVAILABLE)
            total_score += score
            print(f"'{word}' is valid! Score: {score}")
        else:
            print(f"'{word}' is not vaild")

    print(f"\nTotal score: {total_score}")
