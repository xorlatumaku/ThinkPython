# Date: 06/05/2025
# Program to demonstrate the use of logical operators

x = 5
y = 7
print("The value is", x > 0 and x < 10)
print("The value is", x % 2 == 0 or x % 3 == 0)
print("The value is", not x > y)
print("The value is", 42 and True)
print("The value is", 0 and True)

# If statement
if x > 0:
    print("x is positive")

if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")
