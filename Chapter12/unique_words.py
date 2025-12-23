# Date : 06/10/2025
# Program to implement text analysis and generation

import unicodedata

filename = 'dr_jekyll.txt'
unique_words = {}
for line in open(filename):
    seq = line.split()
    for word in seq:
        unique_words[word] = 1

print(len(unique_words))

print(sorted(unique_words, key=len)[-5:])

def split_line(line):
    return line.replace('-', ' ').split()

print(split_line('coolness-fightened'))
print()
print(unicodedata.category('A'))
print(unicodedata.category('.'))

punc_marks = {}
for line in open(filename):
    for char in line:
        category = unicodedata.category(char)
        if category.startswith('P'):
            punc_marks[char] = 1
punctuation = ''.join(punc_marks)
print(punctuation)
print()

def clean_word(word):
    return word.strip(punctuation).lower()
print(clean_word('"Behold!"'))
print(clean_word('pocket-handkerchief'))
print()

unique_word2 = {}
for line in open(filename):
    for word in split_line(line):
        word = clean_word(word)
        unique_word2[word] = 1

print(len(unique_word2))

print(sorted(unique_word2, key=len)[-10:])
print()

# word frequencies
word_counter = {}
for line in open(filename):
    for word in split_line(line):
        word = clean_word(word)
        if word not in word_counter:
            word_counter[word] = 1
        else:
            word_counter[word] += 1

def second_element(t):
    return t[1]

items = sorted(word_counter.items(), key=second_element, reverse=True)

for word, freq in items[:5]:
    print(freq, word, sep='\t')

print()

# Optional parameters
print(round(3.141592653589793, ndigits=3))
print()

def print_most_common(word_counter, num=5):
    items = sorted(word_counter.items(), key=second_element, reverse=True)

    for word, freq in items[:num]:
        print(freq, word, sep='\t')

print_most_common(word_counter)
print()
print_most_common(word_counter, 3)
print()
# Dictionary subtraction
word_list = open('words.txt').read().split()
valid_words = {}
for word in word_list:
    valid_words[word] = 1

def subtract(d1, d2):
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = d1[key]
    return res
diff = subtract(word_counter, valid_words)
print_most_common(diff)
print()
singletons = []
for word, freq in diff.items():
    if freq == 1:
        singletons.append(word)

print(singletons[-5:])
print()

import random
t = [1, 2, 3]
print(random.choice(t))

words = list(word_counter)
print(random.choice(words))
print()

for i in range(6):
    word = random.choice(words)
    print(word, end=' ')

weights = word_counter.values()
print(random.choices(words, weights= weights))

random_words = random.choices(words, weights=weights, k=6)
print(random_words)
print(' '.join(random_words))
print()

# Bigrams
bigram_counter = {}
def count_bigram(bigram):
    key = tuple(bigram)
    if key not in bigram_counter:
        bigram_counter[key] = 1
    else:
        bigram_counter[key] += 1

window = []
def process_word(word):
    window.append(word)

    if len(window) == 2:
        count_bigram(window)
        window.pop(0)

for line in open(filename):
    for word in split_line(line):
        word = clean_word(word)
        process_word(word)
print_most_common(bigram_counter)

bigrams = list(bigram_counter)
weights = bigram_counter.values()
random_bigrams = random.choices(bigrams, weights=weights, k=6)
for pair in random_bigrams:
    print(' '.join(pair), end=' ')


print()
# Date: 06/11/2025
# Program to implement Markov Analysis

song = """
Half a bee, philosophically,
Must, ipso facto, half not be.
But half the bee has got to be
Vis a vis, its entity. D' you see?
"""

successor_map = {}

first = 'half'
second = 'a'

successor_map[first] = [second]
print(successor_map)

first = 'half'
second = 'not'

successor_map[first].append(second)
print(successor_map)

def add_bigram(bigram):
    first, second = bigram

    if first not in successor_map:
        successor_map[first] = [second]
    else:
        successor_map[first].append(second)

def process_word_bigram(word):
    window.append(word)

    if len(window) == 2:
        add_bigram(window)
        window.pop(0)

successor_map = {}
window = []

for word in song.split():
    word = clean_word(word)
    process_word_bigram(word)

print(successor_map) 
# Date: 06/11/2025
# Program to implement Markov Analysis

song = """
Half a bee, philosophically,
Must, ipso facto, half not be.
But half the bee has got to be
Vis a vis, its entity. D' you see?
"""

successor_map = {}

first = 'half'
second = 'a'

successor_map[first] = [second]
print(successor_map)

first = 'half'
second = 'not'

successor_map[first].append(second)
print(successor_map)

def add_bigram(bigram):
    first, second = bigram

    if first not in successor_map:
        successor_map[first] = [second]
    else:
        successor_map[first].append(second)

def process_word_bigram(word):
    window.append(word)

    if len(window) == 2:
        add_bigram(window)
        window.pop(0)

successor_map = {}
window = []

for word in song.split():
    word = clean_word(word)
    process_word_bigram(word)

print(successor_map)
print()

# Analyzing the book
successor_map = {}
window = []

for line in open(filename):
    for word in split_line(line):
        word = clean_word(word)
        process_word_bigram(word)

print(successor_map['going'])

word = 'although'
successors = successor_map[word]
print(successors)

word = random.choice(successors)
print(word)

for i in range(10):
    successors = successor_map[word]
    word = random.choice(successors)
    print(word, end=' ')
