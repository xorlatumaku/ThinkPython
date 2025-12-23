# Date: 06/04/2025
# Program to draw a rectangle with the given width and height

def rectangle(char_str, width, height):
    # Loop height number of times
    for i in range(height):
        # Print the string repeated width times
        print(char_str * width)

# Test the function
rectangle("H", 5, 4) # Creates a 5x4 rectangle of "H"
rectangle("*", 3, 2) # Creates a 3x2 rectangle of stars
rectangle("AB", 4, 3) # Creates a 4x3 rectangle using "AB"
