# Date: 06/09/2025
# Program to find words with no duplicate letters
def has_duplicates(sequence):
    """
    Check if any element in the sequence appears more than once.
    Returns True if there are duplicates, False otherwise.
    """
    return len(sequence) != len(set(sequence))

def find_no_duplicate_words(word_list):
    """
    Find all words where each letter appears only once.
    Returns a dictionary with word lengths as keys and lists of words as values.
    """

    result = {}
    for word in word_list:
        # Convert to lowercase to handle case-insensitive comparison
        word = word.lower().strip()
        if not has_duplicates(word):
            length = len(word)
            if length not in result:
                result[length] =[]
            result[length].append(word)
    return result

# Sample word list 
word_list = [
        "unpredictably",
        "copyrightable",
        "dermatoglyphics",
        "uncopyrightable",
        "ambidextrous",
        "blacksmith",
        "complicated",
        "downstream",
        "background",
        "pneumonia",
        "python",
        "quick",
        "jump",
        "programming",
        "computer",
        "algorthm",
        "duplicate"
    ]

# Test has_duplicates function
print("Testing has_duplicates function:")
test_sequences = [
        "hello",            # has duplicates ('l')
        "world",            # no duplicates
        "programming",      # has duplicates ('r', 'g', 'm')
        "uncopyrightable",  # no duplicates
        [1, 2, 3, 3, 4],    # has duplicates (3)
        [1, 2, 3, 4, 5],    # no duplicates
        "aaa",              # has duplicates ('a')
        "abc",              # no duplicates
    ]

for seq in test_sequences:
    result = has_duplicates(seq)
    print(f"'{seq}': {'has' if result else 'has no'} duplicates")

print("\nFinding words with no duplicate letters:")
no_duplicates = find_no_duplicate_words(word_list)

# Print results sorted by length (longest first)
print("\nWords with no duplicate letters (sorted by length):")
print("-" * 50)
for length in sorted(no_duplicates.keys(), reverse=True):
    words = no_duplicates[length]
    print(f"\n{length} letters:")
    for word in sorted(words):
        print(f"-{word}")

# Find the longest word(s)
if no_duplicates:
    max_length = max(no_duplicates.keys())
    print("\nLongest word(s) with no duplicate letters:")
    print("-" * 50)
    for word in sorted(no_duplicates[max_length]):
        print(f"- {word} ({max_length} letters)")
