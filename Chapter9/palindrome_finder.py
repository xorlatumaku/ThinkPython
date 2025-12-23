# Date: 06/07/2025
# Program  to find palindromes 

def reverse_word(word):
    """Returns the word in reverse order."""
    return ''.join(reversed(word))

def is_palindrome(word):
    """
    Check if a word is a palindrome.
    Returns True if the word reads the same forwards and backwards.
    """
    # Convert to lowercase to make comparison case-insensitive
    word = word.lower().strip()
    return word == reverse_word(word)

# Sample word list (you can expand this or read from a file)
word_list = [
        "rotator", "noon", "python", "level", "madam",
        "racecar", "palindrome", "deified", "reviver",
        "kayak", "elephant", "stats", "computer", "deed",
        "repaper", "reference", "ceremony"
        ]

# Find palindromes with at least 7 letters
print("Palindromes with at least 7 letters:")
for word in word_list:
    if len(word) >=7 and is_palindrome(word):
        print(f"- {word} (length: {len(word)})")

# Test the functions with some examples
print("\nTesting palindrome detection:")
test_words = ["noon", "python", "racecar", "madam", "hello", "deified", "A man a plan a canal Panama"]
for test_word in test_words:
    is_pal = is_palindrome(test_word)
    print(f"'{test_word}': {'is' if is_pal else 'is not'} a palindrome")

# Demonstration of reverse_word function
print("\nDemonstration of reverse_word function:")
demo_words = ["python", "programming", "level"]
for word in demo_words:
    reversed_word = reverse_word(word)
    print(f"'{word}' reversed is '{reversed_word}'")

