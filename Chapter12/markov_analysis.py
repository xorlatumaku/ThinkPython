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
