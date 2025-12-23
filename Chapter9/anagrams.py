# Date: 06/07/2025
# Program to find anagrams

def is_anagram(str1, str2):
    # Convert strings to lowercase and remove any whitespace
    str1 = str1.lower().strip()
    str2 = str2.lower().strip()

    # Sort the characters of both strings and compare them
    return sorted(str1) == sorted(str2)

# Test the function with 'takes' and find its anagrams
word = "takes"
test_words = ["stake", "steak", "break", "skate", "speak", "takes"]

print(f"Finding anagrams for '{word}':")
anagrams = [w for w in test_words if is_anagram(word, w) and w != word]
print(f"Anagrams found: {anagrams}")

# Test cases
print("\nTesting is_anagram function:")
test_cases = [
        ("takes", "stake"),
        ("hello", "world"),
        ("python", "typhon"),
        ("listen", "silent")
    ]

for test_str1, test_str2 in test_cases:
    result = is_anagram(test_str1, test_str2)
    print(f"'{test_str1}' and '{test_str2}' are{' ' if result else ' not '}anagrams")
