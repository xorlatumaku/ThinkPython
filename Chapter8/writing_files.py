# Date 06/07/2025
# Program to implement writing files

reader = open('pg345.txt')
def is_special_line(line):
    return line.startswith('***')
for line in reader:
    if is_special_line(line):
        print(line.strip())

print()

reader = open('pg345.txt')
writer = open('pg345_cleaned.txt', 'w')

for line in reader:
    if is_special_line(line):
        break

for line in reader:
    if is_special_line(line):
        break
    writer.write(line)

reader.close()
writer.close()

for line in open('pg345_cleaned.txt'):
    line = line.strip()
    if len(line) > 0:
        print(line)
    if line.endswith('Stoker'):
        break

print()

total = 0
for line in open('pg345_cleaned.txt'):
    total += 1
print(total)

print()

total = 0 
for line in open('pg345_cleaned.txt'):
    if 'Jonathan' in line:
        total += 1
print(total)

print()

total = 0
for line in open('pg345_cleaned.txt'):
    total += line.count('Jonathan')
print(total)

print()

writer = open('pg345_replaced.txt', 'w')

for line in open('pg345_cleaned.txt'):
    line = line.replace('Jonathan', 'Thomas')
    writer.write(line)

print()

text = "I am Dracula; and I bid you welcome, Mr. Harker, to my house."
pattern = 'Dracula'

import re

result = re.search(pattern, text)
print(result)
print(result.string)
print(result.group())
print(result.span())
print()

result = re.search('Count', text)
print(result)
print()

result == None

def find_first(pattern):
    for line in open('pg345_cleaned.txt'):
        result = re.search(pattern, line)
        if result != None:
            return result

result = find_first('Harker')
print(result.string)

pattern = r'Mina|Murray'
result = find_first(pattern)
print(result.string)

def count_matches(pattern):
    count = 0
    for line in open('pg345_cleaned.txt'):
        result = re.search(pattern, line)
        if result != None:
            count += 1
    return count
print(count_matches('Mina|Murray'))
result = find_first('^Dracula')
print(result.string)

result = find_first('Harker$')
print(result.string)

pattern = 'cent(er|re)'
result = find_first(pattern)
print(result.string)

pattern = 'colou?r'
result = find_first(pattern)
line = result.string
print(line)

print(re.sub(pattern, 'color', line))
