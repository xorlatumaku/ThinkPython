# Date: 06/09/2025
# Program to identify interlocking words.
def is_interlocking(word):
    """
    Check if a word can be split into two interlocking words.
    Returns True if both parts are valid words, False otherwise.
    """
    # Get alternating letters
    first = word[0::2] # starts at index 0, takes every 2nd letter
    second = word[1::2] # starts at index 1, takes every 2nd letter

    # Check if both parts are in the word list
    return first in word_list and second in word_list

def load_word_list(filename='words.txt'):
    """Load words from a file into a set for quick lookup."""
    try:
        with open(filename, 'r') as file:
            return set(word.strip().lower() for word in file)
    except FileNotFoundError:
        # If file not found, use a sample word list
        return sample_word_list

# Sample word list (in case file is not available)
sample_word_list = {
        'shoe', 'cold', 'schooled',
        'under', 'pig', 'underpaid',
        'tap', 'her', 'tapper',
        'can', 'die', 'candied',
        'pin', 'ear', 'pineal',
        'shoe', 'cold', 'schooled',
        'this', 'that', 'the',
        'pin', 'ear', 'pine',
        'cat', 'dog', 'pig',
        'tap', 'pet', 'cap'
    }

def find_interlocking_words(words):
    """Find all interlocking words in a given set of words."""
    result = []
    for word in words:
        if len(word) >= 4 and is_interlocking(word): # minimum length of 4 for meaningful splits
            first = word[0::2]
            second = word[1::2]
            result.append((word, first, second))
    return result

# Load word list
word_list = load_word_list()

# Test cases
test_words = [
        'schooled',
        'underpaid',
        'tapper',
        'candied',
        'father',
        'pineal',
        'python',
        'programming',
        'computer',
        'algorithm',
        'testing'
    ]

print("Testing is_interlocking function:")
print("-" * 50)
for word in test_words:
    is_interlocking_word = is_interlocking(word)
    if is_interlocking_word:
        first = word[0::2]
        second = word[1::2]
        print(f"'{word}' is interlocking:")
        print(f" First word: '{first}'")
        print(f" Second word: '{second}'")
    else:
        print(f"'{word}' is not interlocking")
    print("-" * 50)

# Find all interlocking words in our word list
print("\nFinding all interlocking words in the word list:")
interlocking_words = find_interlocking_words(word_list)

if interlocking_words:
    print("\nAll interlocking words found:")
    print("-" * 50)
    # Sort by word length (longest first)
    for word, first, second in sorted(interlocking_words, key=lambda x: len(x[0]), reverse=True):
        print(f"'{word}' = '{first}' + '{second}'")
else:
    print("No interlocking words found in the word list.")

# Demonstrate slice operations
print("\nDemonstrating slice operations:")
demo_word = "schooled"
print(f"\nWord: '{demo_word}'")
print(f"First part word[0::2]: '{demo_word[0::2]}'")
print(f"Second part word[1::2]: '{demo_word[1::2]}'") 

