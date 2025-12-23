# Date: 06/11/2025
# Program to generate random text using the Markov chain model 

import random
from typing import Dict, List,Tuple

def generate_text_bigrams(successor_map: Dict[Tuple[str, str], List[str]], num_words: int = 50) -> str:
    """
    Generate random text using bigram-based Markov chains.

    Args: 
        successor_map: Dictionary mapping bigrams to their possible successors
        num_words: Number of words to generate
    Returns:
        Generated text as a string
    """
    if not successor_map:
        return "Error: Empty successor map"

    # Choose a random starting bigram
    successors = list(successor_map.keys())
    bigram = random.choice(successors)

    # Initialize the result with the fisrt two words
    generated_words = list(bigram)

    # Generate the specified number of additional words
    for _ in range(num_words):
        # Look up possible successors for current bigram
        possible_successors = successor_map.get(bigram, [])

        # If no successors found, choose a new random bigram
        if not possible_successors:
            bigram = random.choice(successors)
            continue

        # Choose a random successor
        next_word = random.choice(possible_successors)
        generated_words.append(next_word)

        # Create new bigram for next iteration
        bigram = (bigram[1], next_word)

    return ' '.join(generated_words)

# Now let's implement the trigram version
def generate_text_trigrams(successor_map: Dict[Tuple[str, str, str], List[str]], num_words: int = 50) ->
    """
    Generate random text using trigram-based Markov chains.

    Args:
        successors_map: Dictionary mapping trigrams to their possible successors
        num_words: Number of words to generate

    Returns:
        Generated text as a string
    """
    if not successor_map:
        return "Error: Empty successor map"

    # Choose a random starting trigram
    successors = list(successor_map.keys())
    trigram = random.choice(successors)

    # Initialize the result with the first three words
    generated_words = list(trigram)

    # Generate the speciified number of additional words
    for _ in range(num_words):
        # Look up possible successors for current trigram
        possible_successors = successor_map.get(trigram, [])

        # If no successors found, choose a new random trigram
        if not possible_successors:
            trigram = random.choice(successors)
            continue
        
        # Choose a random successor
        next_word = random.choice(possible_successors)
        generated_words.append(next_word)

        # Create new trigram for next iteration
        trigram = (trigram[1], trigram[2], next_word)

    return ' '.join(generated_words)
