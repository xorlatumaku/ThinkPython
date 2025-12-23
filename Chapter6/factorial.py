# Date: 06/05/2025
# Program to demonstrate a recursive function with factorial
def factorial(n):
    """Input Validation"""
    if not isinstance(n, int):
        print("factorial is only defined for integers.")
        return None
    elif n < 0:
        print("factorial is not defined for negative numbers.")
        return None
    elif n == 0:
        return 1
    else:
        recurse = factorial(n - 1)
        return n * recurse

# Testing result
print("5! = ", factorial(5))
factorial("Max Planck")
factorial(-2)

# Scaffolding factorial
def facatorial(n):
    space = " " * (4 * n)
    print(space, "factorial", n)
    if n == 0: 
        print(space, "returning 1")
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        print(space, "returning", result)
        return result
# Result
factorial(3)

