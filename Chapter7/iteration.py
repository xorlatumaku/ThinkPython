# Date: 06/05/2025
# Program to demonstrate iteration and search

for letter in "Planck":
    print(letter, end=" ")
    
print()

def has_e(word):
    if "E" in word or "e" in word:
        return True
    else:
        return False
print(has_e("Planck"))
print(has_e("Max"))
print(has_e("Emma"))
print()

""" Program to count the number of words that contain an 'e' """
total = 0
count = 0

for line in open("words.txt"):
    word = line.strip()
    total += 1
    if has_e(word):
        count += 1
print("Total number of words: ", total)
print("How many words contain an 'e': ", count)
print("Total percentage of count: ", count / total * 100)

""" Program to search through a word """
def uses_any(word, letters):
    for letter in word.lower():
        if letter in letters.lower():
            return True
    return False
print(uses_any("EINSTEIN", "aeiou"))
print(uses_any("apple", "xyz"))
