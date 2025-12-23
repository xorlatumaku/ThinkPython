# Date: 06/05/2025
# Program to demonstrate recursion

def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n - 1)
countdown(5)
print()
def print_n_times(string, n):
    if n > 0:
        print(string)
        print_n_times(string, n - 1)
print_n_times("Spam", 5)
