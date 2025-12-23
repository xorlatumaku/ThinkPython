# Date: 06/09/2025
# Program to demonstrate the mutability of tuples containing mutable objects and why they can't be used as dictionary keys.

def demonstrate_tuple_mutability():
    """Demonstrate how tuples containing mutable objects can be modified."""
    # Create initial lists and tuple
    list0 = [1, 2, 3]
    list1 = [4, 5]
    t = (list0, list1)

    print("Initial state:")
    print(f"list0 = {list0}")
    print(f"list1 = {list1}")
    print(f"t = {t}")

    # Modify the second list through the tuple
    print("\nAppending 6 to the second list through the tuple:")
    t[1].append(6)
    print(f"t = {t}")

    # Show that the original list1 is also modified
    print("\nOriginal list1 is also modified:")
    print(f"list1 = {list1}")

    return t

def test_hashability():
    """Demonstrates which tuples can cannot be used as dictionary keys."""
    print("\nTesting tuple hashability:")
    print("-" * 50)

    # Test cases - different types of tuples
    test_tuples = [
            ((1, 2, 3), "Tuple of immutable integers"),
            (("a", "b", "c"), "Tuple of immutable strings"),
            ((1, "hello", 2.5), "Tuple of mixed immutable types"),
            (([1, 2], [3, 4]), "Tuple of mutable lists"),
            ((1, [2, 3], 4), "Tuple with a mutable list"),
            ((1, {"a": 1}, 2), "Tuple with a mutable dictionary"),
            (({1, 2}, {3, 4}), "Tuple of immutable sets"),
            ((frozenset([1, 2]), frozenset([3, 4])), "Tuple of immutable frozensets")
    ]

    # Try to use each tuple as a dictionary key
    test_dict = {}
    for t, description in test_tuples:
        try:
            test_dict[t] = "test"
            print(f"Success: {description} can be used as a key")
        except TypeError:
            print(f"Failed: {description} cannot be used as a key")
            print(f"    Tuple:{t}")

def demonstrate_list_modification():
    """Demonstrates different ways to modify lists within tuples."""
    # Create a tuple with multiple lists
    tuple_with_lists = ([1, 2], [3, 4], [5, 6])

    print("\nDemonstrating list modifications within a tuple:")
    print("-" * 50)
    print(f"Initial tuple: {tuple_with_lists}")

    # Different modifications
    modifications = [
            (lambda x: x[0].append(10), "Append to first list"),
            (lambda x: x[1].extend([11, 12]), "Extend second list"),
            (lambda x: x[2].insert(0, 0), "Insert art start of third list"),
            (lambda x: x[0].pop(), "Remove from first list"),
            (lambda x: x[1].clear(), "Clear second list")
    ]

    for modify, description in modifications:
        modify(tuple_with_lists)
        print(f"\nAfter {description}:")
        print(f"tuple = {tuple_with_lists}")

# Main execution
print("Demonstrating tuple mutability and hashability")
print("=" * 50)

# Demonstrate basic tuple mutability
t = demonstrate_tuple_mutability()

# Test hashability of different tuple types
test_hashability()

# Demonstrate various list modifications
demonstrate_list_modification()

