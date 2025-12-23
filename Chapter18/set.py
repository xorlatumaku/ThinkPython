# Date: 06/12/2025
# Program to implement sets
import math
s1 = set()
s1.add('a')
s1.add('b')
print(s1)
print()

s2 = set('acd')
print(s2)
print()

s3 = set('banana')
print(s3)
print()

print(s1.union(s2))
print(s1 - s2)

print(set('ab') <= set('abc'))

from collections import Counter
counter = Counter('banana')
print(counter)
print(counter.most_common())
counter2 = Counter('bans')
print(counter + counter2)
print()

from collections import Counter
t = (1, 1, 1, 2, 2, 3)
counter = Counter(t)
print(counter)
print(counter['d'])
print(counter.most_common())

from collections import defaultdict
d = defaultdict(list)
print(d)
print()

t = d['new key']
print(t)

t.append('new value')
print(d['new key'])
print()

from collections import defaultdict
d = defaultdict(list)
key = ('into', 'the')
d[key].append('woods')
print(d[key])
print()

x = 2
if x > 0:
    y = math.log(x)
else:
    y = float('nan')
print(y)

y = math.log(x) if x > 0 else float('nan')
print(y)
print()

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
print(factorial(5))
print(counter.most_common())
print()

# List Comprehensions
title = 'monty python and the holy grail'
t = []
for word in title.split():
    t.append(word.capitalize())
print(''.join(t))
print()

t = [word.capitalize() for word in title.split()]
print(''.join(t))
print()

print(sum([1/2**n for n in range(10)]))
print()
print(sum(1/2**n for n in range(10)))
print()

print(any(letter == 't' for letter in 'monty'))
