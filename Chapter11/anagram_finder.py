# Date: 06/10/2025
# Program that finds sets of anagrams in a word list.

def find_anagram_sets(word_list):
    """
    Find all sets of anagrams in a list of words.

    Args:
        word_list: List of words to check for anagrams

    Returns:
        List of lists, where each inner list contains words that are anagrams of each other
    """
    # Dictionary to store sorted letters as key and list of words as value
    anagram_map = {}

    # Process each word
    for word in word_list:
        # Convert word to lowercase and sort its letters
        sorted_word = ''.join(sorted(word.lower()))

        # Add word to the list of anagrams for its sorted letters
        if sorted_word in anagram_map:
            anagram_map[sorted_word].append(word)
        else:
            anagram_map[sorted_word] = [word]

    # Return only the sets of words that have anagrams (more than one word)
    return [words for words in anagram_map.values() if len(words) > 1]

def load_word_list(filename='words.txt'):
    """Load words from a file, or return sample words if file not found."""
    try:
        with open(filename, 'r') as file:
            return [word.strip() for word in file]
    except FileNotFoundError:
        return sample_words

# Sample word list for testing
sample_words = [
        'deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled',
        'retainers', 'ternaries',
        'generating', 'greatening',
        'resmelts', 'smelters', 'termless',
        'python', 'typhon',
        'silent', 'listen', 'inlets',
        'binary', 'brainy', 
        'night', 'thing',
        'cat', 'dog', 'bird', # No anagrams
        'state', 'taste', 'seats',
        'reef', 'free',
        'keep' # No anagrams
    ]

def print_anagram_sets(anagram_sets):
    """Print anagram sets in a formatted way."""
    print("\nFound anagram sets:")
    print("=" * 50)

    if not anagram_sets:
        print("No anagrams found.")
        return

    # Sort sets by size (largest first) and then alphabetically
    sorted_sets = sorted(anagram_sets, key=lambda x: (-len(x), x[0].lower()))

    for i, word_set in enumerate(sorted_sets, 1):
        # Sort words within each set
        sorted_words = sorted(word_set)
        print(f"\nSet {i} ({len(sorted_words)} words):")
        print(f"{sorted_words}")

        # Show sorted letters that form these anagrams
        sorted_letters = ''.join(sorted(sorted_words[0].lower()))
        print(f"Sorted letters: '{sorted_letters}'")

def analyze_anagram_sets(anagram_sets):
    """Analyze and print statistics about the anagram sets."""
    if not anagram_sets:
        return

    # Calculate statistics
    total_sets = len(anagram_sets)
    total_words = sum(len(s) for s in anagram_sets)
    largest_set = max(len(s) for s in anagram_sets)
    avg_set_size = total_words / total_sets

    print("\nAnalysis:")
    print("=" * 50)
    print(f"Total number of anagram sets: {total_sets}")
    print(f"Total words in all sets: {total_words}")
    print(f"Largest set size: {largest_set}")
    print(f"Average set size: {avg_set_size:.2f}")

    # Find sets of each size
    size_distribution = {}
    for s in anagram_sets:
        size = len(s)
        size_distribution[size] = size_distribution.get(size, 0) + 1

    print("\nSize distribution:")
    for size in sorted(size_distribution.keys()):
        count = size_distribution[size]
        print(f"{size} words: {count} {'set' if count == 1 else 'sets'}")

# Main execution
print("Anagram Set Finder")
print("=" * 50)

# Load words and find anagram sets
words = load_word_list()
anagram_sets = find_anagram_sets(words)

# Print results
print_anagram_sets(anagram_sets)

# Analyze results
analyze_anagram_sets(anagram_sets)

# Demonstrate the process for a single word
demo_word = "listen"
print(f"\nDemonstrating process for word '{demo_word}':")
print("=" * 50)
sorted_letters = ''.join(sorted(demo_word.lower()))
print(f"Original word: '{demo_word}'")
print(f"Sorted letters: '{sorted_letters}'")

# Find its anagrams
for word_set in anagram_sets:
    if demo_word in word_set:
        print(f"Anagrams found: {word_set}")
        break
