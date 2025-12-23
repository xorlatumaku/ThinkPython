# Date: 06/11/2025
# Program to implement the add_trigram function for Markov chain text analysis that maps bigrams to their successors.

from collections import defaultdict
from typing import List

# Global dictionary to store the mapping from bigrams to possible successors
successor_map = defaultdict(list)

def add_trigram(words: List[str]) -> None:
    """
    Add a trigram to the successor map. The first two words form the key (bigram),
    and the third word is added to the list of possible successors.

    Args:
        words: List of exactly three words forming the trigram
    """
    if len(words) != 3:
        raise ValueError("add_trigram requires exactly three words")

    # Create the key from the first two words
    bigram_key = tuple(words[:2]) # Using tuple since lists can't be dictionary keys

    # Add the third word as a successor
    successor_map[bigram_key].append(word[2])

# The process_word_trigram function you provided
window = [] # Global window to maintain state between calls

def process_word_trigram(word: str) -> None:
    """
    Process each word to create trigrams and update the successor map.

    Args:
        word: The current word being processed
    """
    window.append(word)

    if len(window) == 3:
        add_trigram(window)
        window.pop(0)

def analyze_text(text: str) -> None:
    """
    Analyze text to build the Markov chain model using trigrams.

    Args: 
        text: Input text to analyze
    """

    # Clear any existing data
    successor_map.clear()
    window.clear()

    # Split text into words and process each word
    words = text.split()
    for word in words:
        process_word_trigram(word)

def get_successors(word1: str, word2: str) -> List[str]:
    """
    Get all possible successor words for a given bigram.

    Args:
        word1: First word of the bigram
        word2: Second word of the bigram

    Returns:
        List of all words that follow this bigram in the text
    """
    return successor_map.get((word1, word2), [])

analyze_file('dr_jekyll.txt')
