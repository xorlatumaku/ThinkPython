# Date: 06/08/2025
# Program to implement word list

word_list = open('words.txt').read().split()
print(len(word_list))

def reverse_word(word):
    return ''.join(reversed(word))

word_dict = {}
for word in word_list:
    word_dict[word] = 1

def much_faster():
    count = 0
    for word in word_dict:
        if reverse_word(word) in word_dict:
            count += 1
    return count
print(much_faster())

def value_counts(string):
    counter ={}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter
counter = value_counts('brontosaurus')
print(counter)

counter = value_counts('banana')
print(counter)

for key in counter:
    print(key)

for value in counter.values():
    print(value)

for key in counter:
    value = counter[key]
    print(key, value)

d = {4: ['r', 'o', 'u', 's']}
print(d)

print()

def is_palindrome(word):
    """Check if a word is a palindrome."""
    return reverse_word(word) == word
count = 0
for  word in word_dict:
    if is_palindrome(word):
        count += 1
print(count)

palindromes = []

for word in word_dict:
    if is_palindrome(word):
        palindromes.append(word)

print(palindromes[:10])
print()

long_palindromes = []

for word in palindromes:
    if len(word) >= 7:
        long_palindromes.append(word)

print(long_palindromes)

