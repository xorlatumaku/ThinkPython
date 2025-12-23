# Date: 06/11/2025
# Program to count trigrams in text.

def process_word_trigram(word, previous_words, trigram_dict):
    """
    Process a word to create trigrams with previous words and update the trigram count.

    Args:
        word (str): Current word being processed
        previous_words (list): List containing the last two words processed
        trigram_dict (dict): Dictionary to store trigram counts
    """
    if len(previous_words) == 2:
        # Create trigram from previous two words and current word
        trigram = ' '.join(previous_words + [word])
        # Update count in dictionary
        trigram_dict[trigram] = trigram_dict.get(trigram, 0) + 1

    # Update previous_words list to contain only last two words
    if len(previous_words) < 2:
        previous_words.append(word)
    else:
        previous_words[0] = previous_words[1]
        previous_words[1] = word

def count_trigrams(text):
    """
    Count the frequency of each trigram in the given text.

    Args:
        text (str): Input text to analyze

    Returns:
        dict: Dictionary with trigrams as keys and their counts as values
    """
    # Initialize variables
    words = text.split()
    previous_words = []
    trigram_counts= {}

    # Process each word
    for word in words:
        process_word_trigram(word, previous_words, trigram_counts)
    return trigram_counts

def process_file(filename):
    # Read the file
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower() # Convert to lowercase for consistency

    # Count trigrams
    trigram_counts = count_trigrams(text)

    # Sort and print top trigrams
    sorted_trigrams = sorted(trigram_counts.items(), key=lambda x: x[1], reverse=True)

    print("Top 10 most common trigrams:")
    for trigram, count in sorted_trigrams[:10]:
        print(f'"{trigram}": {count} times')

process_file('dr_jekyll.txt')
