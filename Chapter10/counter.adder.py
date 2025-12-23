# Date: 06/09/2025
# Program to create a function that combines two counter dictionaries

def value_counts(string):
    """Count occurences of each character in a string."""
    counter = {}
    for char in string:
        counter[char] = counter.get(char, 0) + 1
    return counter

def add_counters(counter1, counter2):
    """
    Combines two counter dictionaries by adding their values.

    counter1, counter2: dictionaries mapping elements to counts    returns: new dictionary with combined counts
    """

    result = counter1.copy() # Start with a copy of counter1
    # Add counts from counter2
    for key in counter2:
        result[key] = result.get(key, 0) + counter2[key]
    return result

def print_counter(counter, label):
    """Helper function to print counter contents in a formatted way."""
    print(f"\n{label}:")
    print("-" * 40)
    for char in sorted(counter.keys()):
        print(f"'{char}': {counter[char]}")

# Test cases
test_pairs = [
        ("brontosaurus", "apatosaurus"), # Original example
        ("python", "programming"),       # Programming terms
        ("hello", "world"),              # Common test words
        ("aaa", "bbb"),                  # Repeated letters
        ("", "test"),                    # Empty string test
        ("12345", "54321"),              # Numbers
        ("!!!", "@@@"),                  # Special characters
        ("ABC", "abc")                   # Different cases
    ]

print("Testing add_counters function:")

for word1, word2 in test_pairs:
    print(f"\nCombining counts for'{word1}' and '{word2}':")
    print("=" * 50)

    # Create counters for both words
    counter1 = value_counts(word1)
    counter2 = value_counts(word2)

    # Print individual counters
    print_counter(counter1, f"Counter for '{word1}'")
    print_counter(counter2, f"Counter for '{word2}'")

    # Combine counters and print result
    combined = add_counters(counter1, counter2)
    print_counter(combined, "Combined counter")

    # Print some statistics
    print("\nStatistics:")
    print(f"Total unique characters: {len(combined)}")
    print(f"Maximum count: {max(combined.values()) if combined else 0}")
    if combined:
        most_common = max(combined.items(), key=lambda x:x[1])
        print(f"Most common character: '{most_common[0]}' ({most_common[1]} times)")

