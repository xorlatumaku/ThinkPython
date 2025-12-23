# Date: 06/05/2025
# Program to demonstrate incremental developement
import math

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    print("dx is: ", dx)
    print("dy is: ", dy)
    dsquared = dx**2 + dy**2
    print("dsquared is: ", dsquared)
    result = math.sqrt(dsquared)
    print("The result is: ",result)

distance(1, 2, 4, 6)

# Program to demonstrate the use of boolean functions
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

print(is_divisible(6,4))
print(is_divisible(6, 3))
