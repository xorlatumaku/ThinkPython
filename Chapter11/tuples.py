# Date: 06/09/2025
# Program to implement tuples

t = 'l', 'u', 'p' , 'i', 'n'
print(type(t))

t1 = 'p',
print(type(t1))

t = tuple('planck')
print(t)
print(t[0])
print(t[1:3])
print(tuple('lup') + ('i', 'n'))
print(tuple('spam') * 2)

# split an email address into a username and domain
email = 'mowpython@gmail.com'
username, domain = email.split('@')
print(username, domain)

# loop through items in a dictionary
d = {'one': 1, 'two':2}

for item in d.items():
    key, value = item
    print(key, '->', value)

for key, value in d.items():
    print(key, '->', value)

quotient, remainder = divmod(7, 3)
print(quotient)
print(remainder)

def min_max(t):
    return min(t), max(t)
print(min_max([2, 4, 1, 3]))

# the following function takes any number of arguments and computes their arithmetic mean 
def mean(*args):
    return sum(args) /len(args)
print(mean(1, 2, 3))
print()

# this function takes any number of arguments, removes the lowest and highest, and computes the mean of the rest:

def trimmed_mean(*args):
    low, high = min_max(args)
    trimmed = list(args)
    trimmed.remove(low)
    trimmed.remove(high)
    return mean(*trimmed)
print(mean(1, 2, 3, 10))
print(trimmed_mean(1, 2, 3, 10))
print()

# using the zip object to loop through the values in the seq.
scores1 = [1, 2, 4, 5, 1, 5, 2]
scores2 = [5, 5, 2, 2, 5, 2, 3]
for pair in zip(scores1, scores2):
    print(pair)
wins = 0
for team1, team2 in zip(scores1, scores2):
    if team1 > team2:
        wins += 1
print(wins)
t = list(zip(scores1, scores2))
print(t)
print(t[-1])
print()

# how to make a dictionary that maps from each letter to its position in the alphabet
letters = 'abcdefghijklmnopqrstuvwxyz'
numbers = range(len(letters))
letter_map = dict(zip(letters, numbers))
print(letter_map['a'], letter_map['z'])
for index, element in enumerate('abc'):
    print(index, element)

# Comparing and sorting
def value_counts(string):
    counter = {}
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter
counter = value_counts('banana')
print(counter)

items = counter.items()
print(items)
print(sorted(items))
def second_element(t):
    return t[1]
sorted_items = sorted(items, key=second_element)
print(sorted_items)
print(sorted_items[-1])
print(max(items, key=second_element))
print()

d = value_counts('parrot')
print(d)

def invert_dict(d):
    new = {}
    for key, value in d.items():
        if value not in new:
            new[value] = [key]
        else:
            new[value].append(key)
    return new
print(invert_dict(d))


