# Date: 06/06/2025
# Program to demonstrate string and regular expressions

greeting = 'Hello, world!'

new_greeting = 'J' + greeting[1:]
print(new_greeting)
print(greeting)

def compare_word(word):
    if word < 'banana':
        print(word, 'comes before banana.')
    elif word > 'banana':
        print(word, 'comes after banana.')
    else:
        print('All right, banana.')
print(compare_word('apple'))
print(compare_word('Pineapple'))

word = 'banana'
new_word = word.upper()
print(new_word)
