# Date: 06/07/2025
# Program to implement a list

letters = ['a', 'b', 'c', 'd', 'e']
letters.append('f')
print(letters)

letters.extend(['g', 'h'])
print(letters)

t = ['a', 'b', 'c']
print(t.pop(1))
print(t)
print(t.remove('c'))
print(t)

s = 'Spam'
t = list(s)
print(t)

s = 'pining for the fjords'
t = s.split()
print(t)

s = 'ex-parrot'
t = s.split('-')
print(t)

delimiter = ' '
t = ['pining', 'for', 'the', 'fjords']
s = delimiter.join(t)
print(s)

# Looping through a list
s = 'pining for the fjords'
for word in s.split():
    print(word)

# Sorting Lists
print()
scramble = ['c', 'a', 'b']
print(sorted(scramble))
print(scramble)
print(sorted('letters'))
print(''.join(sorted('letters')))

# Objects and Values
a = 'banana'
b = 'banana'
print(a is b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)

# Aliasing
a = [1, 2, 3]
b = a
print(b is a)
b[0] = 5
print(a)

print()

# List Arguments
def pop_first(lst):
    return lst.pop(0)
letters = ['a', 'b', 'c']
print(letters)
print(pop_first(letters))
print(letters)

