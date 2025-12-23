# Date: 06/11/2025
# Program to create and test a function to replace text in files.Let's break this down into two parts.

def replace_all(pattern, replacement, input_file, output_file):
    """
    Read contents from input_file, replace all occrrences of pattern with replacement, and write the result to output_file.

    Args:
        pattern (str): The string pattern to search for 
        replacement (str): The string to replace the pattern with
        input_file (str): Path to the input file
        output_file (str): Path to the output file where results will be written
    """
    try:
        # Read the contents of the input file
        with open(input_file, 'r') as f:
            content = f.read()

        # Replace all occurrences of the pattern
        modified_content = content.replace(pattern, replacement)
        # Write the modified content to the output file
        with open(output_file, 'w') as f:
            f.write(modified_content)

    except FileNotFoundError:
        print(f"Error: Could not find the input file '{input_file}'")
    except PermissionError:
        print(f"Error: Permission denied when accessing the files")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    # Test the function with the specified files
    if __name__ == "__main__":
        replace_all('photos', 'images', 'photos/notes.txt', 'photos/new_notes.txt')

def verify_changes():
    with open('photos/notes.txt', 'r') as f:
        original = f.read()
    with open('photos/new_notes.txt', 'r') as f:
        modified = f.read()

    print("Original content:")
    print(original)
    print("\nModified content:")
    print(modified)

verify_changes()
