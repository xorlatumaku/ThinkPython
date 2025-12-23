# Date: 06/05/2025
# Program to demonstrate triangle inequality theorem

def is_triangle(a, b, c):
    """
    Check if three lengths can form a triangle.
    Returns "Yes" if possible, "No" if impossible.
    """

    # Check all three conditions where triangle is impossible
    if a > b + c:
        print("No")
    elif b > a + c:
        print("No")
    elif c > a + b:
        print("No")
    else:
        print("Yes")

# Test cases
print("Test cases:")
print("Sides (3, 4, 5):", end=" ")
is_triangle(3, 4, 5) # Should print Yes (valid triangle)

print("Sides (12, 1, 1):", end=" ")
is_triangle(12, 1, 1) # Should print No (one side too long)

print("Sides (5, 5, 5):", end=" ")
is_triangle(5, 5, 5) # Should print Yes (equilateral triangle)

print("Sides (4, 2, 2):", end=" ")
is_triangle(4, 2, 2) # Should print No (degenerate triangle)

# Allow user input for testing
def test_triangle():
    """Function to test triangle formation with user input"""
    print("\nEnter three stick lengths to check if they can form a triangle:")
    try:
        a = int(input("Length of first stick: "))
        b = int(input("Length of second stick: "))
        c = int(input("Length of third stick: "))
        print("Can these sticks form a triangle?", end=" ")
        is_triangle(a, b, c)
    except ValueError:
        print("Please enter valid integer lengths.")

# Run interactive test if desired
test_triangle()
