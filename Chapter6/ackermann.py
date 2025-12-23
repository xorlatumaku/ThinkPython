# Date: 06/05/2025
# Program to demonstrate a recursive function with Ackermann function
""" This Ackermann function is often used as an example of a computable function that's not primitive recursive, meaning it grows faster than any primitive recursive function. It's a good demonstration of the limits of recursive computation in practice."""


def ackermann(m, n):
    """
    Compute Ackermann function A(m,n)

    Parameters:
    m, n: non-negative integers

    Returns:
    Result of Ackermann function
    """
    
    # Base case: if m = 0
    if m == 0:
        return n + 1

    # Case: if m > 0 and n = 0
    elif n == 0:
        return ackermann(m - 1, 1)

    # Case: if m > 0 and n > 0
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

# Test with small values first
print("Testing Ackermann function with small values:")
print(f"A(0,0) = {ackermann(0,0)}") # Should return 1
print(f"A(0,1) = {ackermann(0,1)}") # Should return 2
print(f"A(1,1) = {ackermann(1,1)}") # Should return 3
print(f"A(2,2) = {ackermann(2,2)}") # Should return 7
print(f"A(3,2) = {ackermann(3,2)}") # Should return 29

# Warning about large values
print("\nWarning: A(5,5) will cause:")
print("1. Stack overflow or")
print("2. Very long computation time or")
print("3. System resource exhaustion")
print("This is because the Ackermann function grows extremely rapidly.")
