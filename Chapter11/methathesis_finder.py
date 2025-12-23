# Date: 06/10/2025
# Program to find methathesis pairs in a word list

from collections import defaultdict

def find_metathesis_pairs(word_list):
    """
    Find all metathesis pairs in a list of words.
    A metathesis pair consists of two words that can be transformed into each other by swapping exactly two letters.

    Args:
        word_list: List of words to check

    Returns:
        List of tuples, each containing a metathesis pair
    """
    # First group words by their sorted letters (anagrams)
    anagram_map = defaultdict(list)
    for word in word_list:
        # Convert to lowercase and sort letters
        sorted_word = ''.join(sorted(word.lower()))
        anagram_map[sorted_word].append(word)

    # Find metathesis pairs within each anagram group
    metathesis_pairs = []

    for anagram_group in anagram_map.values():
        # Only check groups with at least 2 words
        if len(anagram_group) < 2:
            continue

        # Compare each pair of words in the group
        for i in range(len(anagram_group)):
            for j in range(i + 1, len(anagram_group)):
                word1 = anagram_group[i].lower()
                word2 = anagram_group[j].lower()

                if is_metathesis_pair(word1, word2):
                    metathesis_pairs.append((anagram_group[i], anagram_group[j]))
    return metathesis_pairs

def is_metathesis_pair(word1, word2):
    """
    Check if two words form a metathesis pair.
    Returns True if exactly two letters need to be swapped to transform one word into the other.
    """
    if len(word1) != len(word2):
        return False

    # Find positions where letters differ
    differences = [(i, word1[i], word2[i])
                   for i in range(len(word1))
                   if word1[i] != word2[i]]

    # Check if exactly two positions differ
    if len(differences) != 2:
        return False

    # Check if swapping the letters works
    pos1, letter1_1, letter1_2 = difference[0]
    pos2, letter2_1, letter2_2 = difference[1]

    # Verify that swapping these letters transforms one word into the other
    return letter1_1 == letter2_2 and letter2_1 == letter1_2

def load_word_list(filename='words.txt'):
    """Load words from a file, or return sample words if file not found."""
    try:
        with open(filename, 'r') as file:
            return [word.strip() for word in file]
    except FileNotFoundError:
        return sample_words

# Sample word list for testing
sample_word = [
        'converse', 'converse',
        'least', 'steal',
        'silent', 'listen',
        'rescue', 'secure',
        'python', 'typhon',
        'night', 'thing',
        'state', 'taste',
        'parts', 'traps',
        'points', 'joints',
        'earth', 'heart',
        'cease', 'peace',
        'unite', 'untie',
        'tear', 'rate',
        'kitchen', 'thicken'
    ]

def print_metathesis_pairs(pairs):
    """Print metathesis pairs in a formatted way."""
    print("\nFound metathesis pairs:")
    print("=" * 50)

    if not pairs:
        print("No metathesis pairs found.")
        return

    # Sort pairs by word length and alphabetically
    sorted_pairs = sorted(pairs, key=lambda x: (len(x[0]), x[0].lower()))
    
    for i, (word1, word2) in enumerate(sorted_pairs, 1):
        print(f"\nPair {i}:")
        # Find the positions where letters differ
        differences = [(i, word1[i], word2[i])
                       for i in range(len(word1))
                       if word1[i] != word2[i]]

        # Show the words and highlight the swapped letters
        print(f"Word 1: {word1}")
        print(f"Word 2: {word2}")
        pos1, letter1_1, _ = differences[0]
        pos2, letter2_1, _ = differences[1]
        print(f"Swapped letters: '{letter1_1}' at position {pos1+1} with '{letter2_1}' at position {pos2+1}")

def analyze_metathesis_pairs(pairs):
    """Analyze and print statistics about the metathesis pairs."""
    if not pairs:
        return

    # Calculate statistics
    word_lengths = [len(pair[0]) for pair in pairs]
    avg_length = sum(word_lengths) / len(word_lengths)

    print("\nAnalysis:")
    print("=" * 50)
    print(f"Total number of metathesis pairs: {len(pairs)}")
    print(f"Average word length: {avg_length:.2f}")

    # Group pairs by word length
    length_distribution = defaultdict(int)
    for pair in pairs:
        length_distribution[len(pair[0])] += 1

    print("\nLength distribution:")
    for length in sorted(length_distribution.keys()):
        count = length_distribution[length]
        print(f"{length} letters: {count} {'pair' if count == 1 else 'pairs'}")

    # Main execution
    print("Metathesis Pair Finder")
    print("=" * 50)

    # Load word and find metathesis pairs
    words = load_word_list()
    metathesis_pairs = find_metathesis_pairs(words)

    # Print results
    print_metathesis_pairs(metathesis_pairs)

    # Demonstrate the process for a pair
    demo_pair = ('converse', 'conserve')
    print("\nDemonstrating process for pair {demo_pair}:")
    print("=" * 50)
    print(f"Checking if words are anagrams...")
    sorted1 = ''.join(sorted(demo_pair[0].lower()))
    sorted2 = ''.join(sorted(demo_pair[1].lower()))
    print(f"Sorted letters for {demo pair[0]}: {sorted1}")
    print(f"Sorted letters for {demo pair[1]}: {sorted2}")
    print(f"Are they anagrams? {sorted1 == sorted2}")
    print("\nChecking letter differences...")
    differences = [(i, demo_pair[0][i], demo_pair[1][i])
                   for i in range(len(demo_pair[0]))
                   if demo_pair[0][i] != demo_pair[1][i]]
    print(f"Differing positions: {differences}")

