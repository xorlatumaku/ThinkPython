# Date: 06/05/2025
# Program to demonstrate a recursive function with fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# Outputing result
print("Fibonacci(5) = ", fibonacci(5))

