# Date: 06/05/2025
# This program implements the Euclidean algorithm for finding the Greatest Common Divisor (GCD) of two numbers

def gcd(a, b):
    """
    Calculate the Greatest Common Divisor of a and b using Euclidean algorithm.

    Parameters:
    a, b: integers (b can be 0)

    Returns:
    The greatest common divisor of a and b
    """

    # Handle negative numbers by using absolute values
    a = abs(a)
    b = abs(b)

    # Base case: if b is 0, return a
    if b == 0:
        return a

    # Recursive case: gcd(a,b) = gcd(b,r) where r is remainder of a/b
    r = a % b
    return gcd(b,r)

# Test cases
print("Testing GCD function:")
print(f"GCD of 48 and 18 = {gcd(48, 18)}")  # Should be 6
print(f"GCD of 54 and 24 = {gcd(54, 24)}")  # Should be 6
print(f"GCD of 42 and 56 = {gcd(42, 56)}")  # Should be 14
print(f"GCD of 0 and 8 = {gcd(0, 8)}")      # Should be 8
print(f"GCD of 8 and 0 = {gcd(8,0)}")       # Should be 8
print(f"GCD of -48 and 18 = {gcd(-48, 18)}") # Should be 6
print(f"GCD of 48 and -18 = {gcd(48, -18)}") # Should be 6
