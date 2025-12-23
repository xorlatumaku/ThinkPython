# Date:06/09/2025
# Program to implement a Caesar cipher using the letter mappingapproach

def create_letter_map():
    """Creates a dictionary mapping letters to their positions in the alphabet."""
    letters = 'abcdefghijklmnopqrstruvwxyz'
    numbers = range(len(letters))
    return dict(zip(letters, numbers)), letters

def shift_word(word, shift):
    """
    Encrypts a word using a Caesar cipher with the specified shift.

    Args:
        word: The word to encrypt (string)
        shift: Number of positions to shift each letter (integer)

    Returns:
        The encrypted word (string)
    """
    # Get letter mapping and alphabet
    letter_map, letters = create_letter_map()

    # Initialize list to store shifted letters
    shifted_letters = []

    # Process each letter in the word
    for char in word.lower():
        if char in letter_map:
            # Get position of current letter
            position = letter_map[char]

            # Calculate new position with wrap-around using modulo
            new_position = (position + shift) % 26

            # Get new letter and append to result
            shifted_letters.append(letters[new_position])
        else:
            # Keep non-letter characters unchanged
            shifted_letters.append(char)
    
    # Join the shifted letters into a word
    return ''.join(shifted_letters)

def decode_word(encoded_word, shift):
    """Decodes a Caesar cipher by shifting in the opposite direction."""
    return shift_word(encoded_word, -shift)

# Test cases
test_cases = [
        ("cheer", 7, "jolly"),      # cheer jolly
        ("melon", 16, "cubed"),     # melon cubed
        ("hello", 1, "ifmmp"),      # basic shift
        ("zebra", 1, "afcsb"),      # wrap around test
        ("Python", 13, "clguba"),   # mixed case
        ("abc xyz", 1, "bcd yza")   # spaces and wrap-around
    ]

print("Testing Caesar Cipher Implementation")
print("=" * 50)

# Test each case
print("Testing shift_word function:")
print("-" * 50)
for original, shift, expected in test_cases:
    result = shift_word(original, shift)
    decoded = decode_word(result, shift)
    print(f"\nOriginal: '{original}'")
    print(f"Shift: {shift}")
    print(f"Encoded: '{result}'")
    print(f"Decoded: '{decoded}'")
    if result == expected:
        print("Matches expected output")
    else:
        print(f" Expected '{expected}'")

# Demonstrate the letter mapping
letter_map, letters = create_letter_map()
print("\nDemonstrating letter mapping:")
print("-" * 50)
print("Letter positions:")
for letter in 'abcdefghijklmnopqrstruvwxyz':
    print(f"'{letter}' -> {letter_map[letter]}", end=' ')
    if(letter_map[letter] + 1) % 5 == 0:
        print() # New line every 5 letters

# Interactive demonstration
print("\nInteractive demonstration:")
print("-" * 50)
word = "hello"
print(f"\nStarting word: '{word}'")
print("Shifting through positions 1-5:")
for shift in range(1, 6):
    encoded = shift_word(word, shift)
    print(f"Shift {shift}: '{encoded}'")
