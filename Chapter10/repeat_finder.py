# Date: 06/09/2025
# Program to implement the find-repeats function to identify keys with counts greater than 1

def find_repeats(counter):
    """Makes a list of keys with values greater than 1.
    
    counter: dictionary that maps from keys to counts
    returns: list of keys 
    """

    return [key for key in counter if counter[key] > 1]

def value_counts(sequence):
    """Helper function to count occurrences of elements in a sequence."""
    counter = {}
    for item in sequence:
        counter[item] = counter.get(item, 0) + 1
    return counter

def print_results(sequence, counter, repeats):
    """Helper function to print results in a formatted way."""
    print(f"\nAnalyzing sequence: {sequence}")
    print("-" * 50)
    print("Counts dictionary:")
    for key in sorted(counter.keys()):
        print(f"'{key}': {counter[key]}")
    print("\nRepeated elements (count > 1):")
    if repeats:
        for key in sorted(repeats):
            print(f"'{key}' appears {counter[key]} times")
    else:
        print("No repeated elements found")
    print("-" * 50)

# Test cases
test_cases = [
        "brontosaurus",         # string with repeated letters
        "python",               # string with no repeated letters
        [1, 2, 2, 3, 3, 4],     # list with multiple repeats
        [1, 2, 3, 4, 5],        # list with no repeats
        "programming",          # string with multiple repeated letters
        "",                     # empty string
        "aaa",                  # string with same letter repeated
        [1, 1, 1, 1],           # list with same number repeated
        "Hello World!",          # string with spaces and mixed case
        [1, "a", 1, "a", 2, "b"]    # mixed type list
    ]

print("Testing find_repeats function:")

for test_case in test_cases:
    # Get the counts
    counter = value_counts(test_case)

    # Find the repeats
    repeats = find_repeats(counter)

    # Print results
    print_results(test_case, counter, repeats)

# Additional test with custom dictionary
custom_counters = [
        {'a': 3, 'b': 1, 'c':2, 'd':4},
        {'x':1, 'y':1, 'z':1},
        {'word':5, 'sentence':2, 'paragraph':1},
        {} # empty dictionary
]

print("\nTesting with custom dictionaries:")
for counter in custom_counters:
    repeats = find_repeats(counter)
    print(f"\nCounter dictionary: {counter}")
    print("Repeated keys (count > 1):", repeats)
