# Date: 06/04/2025
# Program to calculate trigonometric rule
import math

# Value of x in radians (42 degrees converted to radians)
x = math.radians(42)

# Compute cosine squared of x
cos_squared = math.cos(x) ** 2

# Compute sine squared of x
sin_squared = math.sin(x) ** 2

# Compute the sum of squares
sum_squares = cos_squared + sin_squared

# Display the results
print(f"For x = 42 degrees ({x:.4f} radians):")
print(f"cos^2(x) = {cos_squared:.10f}")
print(f"sin^2(x) = {sin_squared:.10f}")
print(f"cos^2(x) + sin^2(x) = {sum_squares:.10f}")
