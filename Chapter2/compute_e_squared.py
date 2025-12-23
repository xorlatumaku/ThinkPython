# Date: 06/04/2025
# Program to calculate (e squared) using three different methods
import math

# Method 1: Using math.e and ** operator
e_squared_1 = math.e ** 2

# Method 2: Using math.pow
e_squared_2 = math.pow(math.e, 2)

# Method 3: Using math.exp
e_squared_3 = math.exp(2)

# Display results with high precision to see differences
print(f"e^2 computed using math.e ** 2: {e_squared_1:.15f}")
print(f"e^2 computed using math.pow:    {e_squared_2:.15f}")
print(f"e^2 computed using math.exp:    {e_squared_3:.15f}")

# Calculate differences between methods
print("Differences between methods:")
print(f"Method 1 vs Method 2: {abs(e_squared_1 - e_squared_2):.15f}")
print(f"Method 1 vs Method 3: {abs(e_squared_1 - e_squared_3):.15f}")
print(f"Method 2 vs Method 3: {abs(e_squared_2 - e_squared_3):.15f}")
