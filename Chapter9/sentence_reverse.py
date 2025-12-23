# Date: 06/08/2025
# Program to reverse the order of words in a sentence while properly handling capitalization.

def reverse_sentence(sentence):
    """
    Reverses the order of words in a sentence while maintaining proper capitalization. Returns a new string with words in reverse order, first word capitalized, and other words in lowercase.
    """
    #Split the sentence into words and reverse their order
    words = sentence.strip().split()
    reversed_words = words[::-1]

    if not reversed_words: # Handle empty sentence
        return ""

    # Capitalize first word and make others lowercase
    reversed_words[0] = reversed_words[0].capitalize()
    for i in range(1, len(reversed_words)):
        reversed_words[i] = reversed_words[i].lower()

    # Join the words back together with spaces and add a period
    result = " ".join(reversed_words)

    # Add period if the original doesn't end with punctuation
    if not result.endswith(('.', '!', '?')):
        result += '.'

    return result

# Test cases
test_sentences = [
        "Reverse this sentence",
        "Python is an amazing programming language",
        "Hello World",
        "OpenAI ChatGPT helps programmers",
        "The quick brown fox jumps", 
        "", # Empty string test
        "Single", # Single word test
        "THIS IS ALL CAPS",
        "multiple  spaces  between  words",
        "Sentence with a period.",
        "What about questions?",
        "Exclamation marks!"
    ]

# Test the function
print("Testing reverse_sentence function:")
print("-" * 50)
for sentence in test_sentences:
    reversed_sent = reverse_sentence(sentence)
    print(f"Original: '{sentence}'")
    print(f"Reversed: '{reversed_sent}'")
    print("-" * 50)

