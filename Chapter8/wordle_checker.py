# Date: 07/06/2025
# Program to implement a wordle-checker

def check_word(candidate, guesses, feedback):
    """
    Checks if the candidate word matches all Wordle feedback form previous guesses.

    Args:
        candidate (str): A five-letter word to check.
        guesses (list of str): List of previous guessed five-letter words.
        feedback (list of list of str): Each feedback is a list of 5 symbols per guess:
            - 'g' for green (correct position),
            - 'y' for yellow (in word, wrong position),
            - 'b' for black/gray (not in word).

    Returns:
        bool: True if the candidate matches all feedback, False otherwise.

    Example usage:

    # Suppose target is 'MOWER', previous guess is 'TRIED' with feedback:
    # [b, b, b, g, y] ('E' is green at position 3, 'R' is yellow at position 4)
    >>> check_word('MOWER', ['TRIED'], [['b', 'b', 'b', 'g', 'y']])
    True
    >>> check_word('SWEAR', ['TRIED'], [['b', 'b', 'b', 'g', 'y']])
    False
    """

    candidate = candidate.upper()
    for guess, fb in zip(guesses, feedback):
        guess = guess.upper()
        for i in range(5):
            if fb[i] == 'g': # green: must match at this position
                if candidate[i] != guess[i]:
                    return False
            elif fb[i] == 'y': # yellow: must be elsewhere, but not here
                if guess[i] not in candidate or candidate[i] == guess[i]:
                    return False
            elif fb[i] == 'b': # black/gray: must not be in word at all (unless accounted for by previous green/yellow)
                # If guess[i] is green/yellow elsewhere in the guess, allow extra occurrences in candidate
                letter = guess[i]
                # Count how many times letter is 'g' or 'y' in feedback
                allowed = sum(1 for j in range(5) if guess[j] == letter and (fb[j] == 'g' or fb[j] == 'y'))
                # Count total occurrences in candidate
                in_candidate = candidate.count(letter)
                # Only allowed as many as green/yellow occurences
                if in_candidate > allowed:
                    return False
    return True


# Example usage:
if __name__ == "__main__":
    # feedback: 'TRIED' -> [b, b, b, g, y] ( T I D wrong, E correct pos, R in word but not last pos)
    print(check_word('MOWER', ['MOWER'], [['b', 'b', 'b', 'g', 'y']])) # True
    print(check_word('SWEAR', ['MOWER'], [['b', 'b', 'g', 'y']])) # False

    # feedback: 'SPADE' and 'CLERK' -> E is yellow in both, others are black
    guesses = ['SPADE', 'CLERK']
    feedback = [
            ['b','b','b','b','y'], # SPADE: only E is yellow
            ['b','b','b','b','y'], # CLERK: only K is gray, E is yellow at the end
    ]
    print(check_word('MOWER', guesses, feedback)) # True
    print(check_word('WOMEN', guesses, feedback)) # True
    print(check_word('SWEAR', guesses, feedback)) # False
