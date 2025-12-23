# Date: 06/05/2025
# Program to demonstrate integer division and modulus
import math
minutes = 105
hours = minutes / 60
print(hours)

hours = minutes // 60
print(hours)

remainder = minutes - hours * 60
print(remainder)

start = 11
duration = 3
end = (start + duration) % 12
print(end)

a = 25 // 10
b = 25 % 10
print("(",a, b,")")

x = 5
y = 7
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(5 == 5)
print(type(True))
