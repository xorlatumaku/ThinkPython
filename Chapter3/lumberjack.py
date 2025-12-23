# Date: 06/04/2025
# Program to display Monty Python lyrics

def print_lyrics():
    print("I'm a lumberjack,and I'm okay.")
    print("I sleep all night and I work all day.")
print_lyrics()

def print_twice(string):
    print(string)
    print(string)
print_twice("Max Planck,")

string = "Albert Einstein,"
print(string)
print(string)

line = "Geofrey Hinton,"
print_twice(line)

def repeat(word, n):
    print(word *n)

spam = "Spam, "
repeat(spam, 4)

def first_two_lines():
    repeat(spam, 4)
    repeat(spam, 4)

first_two_lines()

def last_three_lines():
    repeat(spam, 2)
    print("(Lovely Spam, Wonderful Spam!)")
    repeat(spam, 2)
last_three_lines()

print()
print()

def print_verse():
    first_two_lines()
    last_three_lines()

print_verse()

for i in range(2):
    print("Verse", i)
    print_verse()
    print()

def catTwice(part1, part2):
    cat = part1 + part2
    print_twice(cat)

line1 = "Always look on the "
line2 = "bright side of life."
catTwice(line1, line2)
