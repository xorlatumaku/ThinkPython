# Date: 06/07/2025
# Program to demonstrate making a word list
word_list = []

for line in open('words.txt'):
    word = line.strip()
    word_list.append(word)

print(len(word_list))

string = open('words.txt').read()
print(len(string))

word_list = string.split()
print(len(word_list))

print('demotic' in word_list)
print('contrafibularities' in word_list)
