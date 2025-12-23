# Date: 06/04/2025
# Program to draw a triangle with a given height

def triangle(char_str, height):
    #Loop from 1 to height (inclusive)
    for i in range(1, height + 1):
        # Print the string repeated i times
        print(char_str * i)

# Test the function
triangle("L", 5)
triangle("*", 5) 
triangle("AB", 5)
