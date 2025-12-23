# Date: 06/04/2025
# Program to print the song "99 Bottles of Beer"

def bottle_line(num_bottles):
    if num_bottles == 1:
        return f"{num_bottles} bottle of beer"
    elif num_bottles == 0:
        return "No more bottles of beer"
    else:
        return f"{num_bottles} bottles of beer"

def bottle_verse(n):
    # First line
    print(f"{bottle_line(n)} on the wall,")

    # Second line
    print(f"{bottle_line(n)}.")

    # Third line
    print("Take one down, pass it around,")

    # Fourth line
    print(f"{bottle_line(n-1)} on the wall.")

# Print the first verse 
print("Single verse example:")
bottle_verse(99)
print()

#Optional: Print the entire song
print("Full song:")
for n in range(99, 0, -1):
    bottle_verse(n)
    print()
