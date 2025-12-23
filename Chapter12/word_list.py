# Date: 06/10/2025
# Program to implement dictionary subtraction
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
