# Date: 06/10/2025
# Program that finds and displays the most frequent letters in a string.

def most_frequent_letters(text):
    """
    Counts and prints letters in a string in decreasing order of frequency.

    Args:
        text: The input string to analyze
    """

    # Count letter frequencies using a dictionary
    freq = {}
    for char in text.lower():
        if char.isalpha(): # Only count letters
            freq[char] = freq.get(char, 0) + 1

    # Sort letters by frequency (highest to lowest)
    # Using sorted with reverse=True and a lambda for the key
    sorted_letters = sorted(freq.items(), key=lambda x: (x[1], x[0]), reverse=True)

    # Print results in a formatted way
    print(f"\nLetter frequencies in '{text}':")
    print("-" * 40)
    print("Letter Count Percentage Visualization")
    print("-" * 40)

    total_letters = sum(freq.values())
    for letter, count in sorted_letters:
        percentage = (count / total_letters) * 100
        bar = '#' * count # Visual representation of frequency        print(f"  {letter}    {count:2d}  {percentage:6.2f}%  {bar}")

    return sorted_letters

def analyze_text(text):
    """
    Performs detailed analysis of letter frequencies in text.
    Returns statistics about the analysis.
    """
    frequencies = most_frequent_letters(text)

    # Calculate statistics
    stats = {
            'total_letters': sum(freq[1] for freq in frequencies),
            'unique_letters': len(frequencies),
            'most_common': frequencies[0] if frequencies else None,
            'least_common': frequencies[-1] if frequencies else None
    }

    # Print statistics
    print("\nAnalysis Statistics:")
    print("-" * 40)
    print(f"Total letters: {stats['total_letters']}")
    print(f"Unique letters: {stats['unique_letters']}")
    if stats['most_common']:
        print(f"Most common letter: '{stats['most_common'][0]}' ({stats['most_common'][1]} times)")
    if stats['least_common']:
        print(f"Least common letter: '{stats['least_common'][0]}' ({stats['least_common'][1]} times)")

    return stats

# Test cases
test_strings = [
        "brontosaurus",
        "programming is fun",
        "Hello World!",
        "The quick brown fox jumps over the lazy dog",
        "aaaaaabbcc", # String with clear frequency pattern
        "UPPER lower MIXED", # Mixed case
        "12345 !@#$ abc", # Mixed with numbers and special characters
        "", # Empty string
    ]

print("Testing most_frequent_letters function:")
print("=" * 60)

# Test each string
for test_string in test_strings:
    print(f"\nTesting string: '{test_string}'")
    stats = analyze_text(test_string)

# Demonstrate different sorting methods
demo_text = "demonstration"
print("\nDemonstrating different sorting methods:")
print("=" * 60)

# Method 1: Using sorted with reverse=True
freq = {}
for char in demo_text.lower():
    if char.isalpha():
        freq[char] = freq.get(char, 0) + 1

print("\nMethod 1: Using sorted with reverse=True:")
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
for letter, count in sorted_freq:
    print(f"'{letter}': {count}")

# Method 2: Using reversed and sorted
print("\nMethod 2: Using reversed and sorted:")
for letter, count in reversed(sorted(freq.items(), key=lambda x: (-x[1], x[0]))):
    print(f"'{letter}': {count}")
    
