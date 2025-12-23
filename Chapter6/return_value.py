# Date: 06/05/2025
# Program to demonstrate return values

import math
radius = math.sqrt(42 / math.pi)
print("Radius",radius)

def circle_area(radius):
    area = math.pi * radius ** 2
    return area
print("The area of the cirlce is ",circle_area(radius))

def repeat(word, n):
    print(word * n)
print(repeat("Ghana, ", 4))

def repeat_string(word, n):
    return word * n
line = repeat_string("Spam, ", 4)
print(line)

