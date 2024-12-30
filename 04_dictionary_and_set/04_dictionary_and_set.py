# ++++++++++ Dictionary in Python ++++++++++

# A dictionary in Python is an unordered collection of items, where each item is stored as a key-value pair. In dictionaries, keys must be unique and immutable (e.g., strings, numbers, or tuples), while values can be of any data type, including lists, other dictionaries, or even functions.

# Empty dictionary
empty_dict = {}

# Dictionary with values. it can hold all data types
my_dict = {
    "user_name": "khrlmln",
    "first_name": "Milan",
    "last_name": "Kharel",
    "age": 20,
    "is_logged_in": True,
    "contact": 9841741474,
    "subjects": ["Python", "JavaScript", "TypeScript"],
    "marks": (75, 85, 96, 73),
}

# ++++++++++ Operations on Dictionaries:

# ++++++++++ 1. Accessing Values: We can access dictionary values by using their corresponding keys.
print(my_dict["first_name"])

# accessing values using get() method
print(f"got a value using get() method: {my_dict.get("first_name")}")

# ++++++++++ 2. Adding or Updating Key-Value Pairs: We can add a new key-value pair or update an existing one.
my_dict["email"] = "milan@example.com"  # Adding a new key-value pair
my_dict["age"] = 25  # Updating an existing value

# using update() method
my_dict.update({"Role": "Programmer"})

# printing to see added & updated values
print(my_dict)

# ++++++++++ 3. Removing Items: There are multiple ways to remove items from a dictionary.

# Using del:
del my_dict["user_name"]

# Using pop():
my_dict.pop("age")

# Using popitem() (removes a random item):
my_dict.popitem()

# Using clear() (removes all items):
# my_dict.clear()  # Clears all items from the dictionary

# ++++++++++ 4. Checking for Keys or Values:
print("first_name" in my_dict)
print("Milan" in my_dict.values())

# ++++++++++ 5. Iterating Through a Dictionary: We can iterate through the keys, values, or key-value pairs in a dictionary.

# Here, keys(), values() & items() are built-in Methods of dictionary

# Keys:
for key in my_dict.keys():
    print(key)

# Values
for value in my_dict.values():
    print(value)

# Key-Value Pairs:
for keys, value in my_dict.items():
    print(f"{keys} = {value}")

# ++++++++++ 6. Copying a Dictionary: We can use the copy() method to create a shallow copy of a dictionary.
copy_dict = my_dict.copy()

# ++++++++++ 7. Nested Dictionaries: Dictionaries can also contain other dictionaries as values, creating a hierarchical structure.
employee = {
    "employee-1": {"name": "Milan Kharel", "age": 25},
    "employee-2": {"name": "Roshan", "age": 24},
}

# Accessing and printing the 'name' value of "employee-1" from the 'employee' dictionary
print(employee["employee-1"]["name"])

# ++++++++++ Set in Python ++++++++++

# A set is an unordered collection of unique elements. It is mutable (we can add or remove items), but the elements themselves must be immutable (e.g., numbers, strings, tuples). we can create a set using curly braces {} or the set() function.

# Note: {} creates an empty dictionary, not a set. Always use set() for an empty set.

# Empty set
empty_set = set()

# Set with values.
my_set = {
    1,
    2,
    2,
    3,
    4,
    4,
    5,
}  # it ignores a duplicate values

# ++++++++++ Basic Set Operations ++++++++++

# ++++++++++ Adding Elements: Use add() to add a single element and update() to add multiple elements.
my_set.add(3)  # Adding a single element

my_set.update([6, 7, 8, 9])  # Adding multiple elements

print(my_set)

# ++++++++++ Removing Elements: We can remove elements using remove(), discard(), or pop().
"""
-> remove() raises an error if the element doesn’t exist.
-> discard() does not raise an error.
-> pop() removes and returns a random element.
"""
# Using remove()
my_set.remove(3)

# Using discard()
my_set.discard(2)

# Using pop()
removed_item = my_set.pop()
print(removed_item)  # Random element removed
print(my_set)

# using clear() to clear sets
my_set.clear()

# ++++++++++ Set Operations ++++++++++

# Python sets support mathematical operations like union, intersection, difference, and symmetric difference.

# ++++++++++ 1. Union (| or union()): Combines all unique elements from two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union using |
print(set1 | set2)

# Union using union()
print(set1.union(set2))

# ++++++++++ 2. Intersection (& or intersection()): Finds common elements between two sets.

# Intersection using &
print(set1 & set2)

# Intersection using intersection()
print(set1.intersection(set2))

# ++++++++++ 3. Difference (- or difference()): Elements that are in one set but not in the other.

# Difference using -
print(set1 - set2)

# Difference using difference()
print(set1.difference(set2))

# ++++++++++ 4. Symmetric Difference (^ or symmetric_difference()): Elements that are in either of the sets but not in both.

# Symmetric Difference using ^
print(set1 ^ set2)

# Symmetric Difference using symmetric_difference()
print(set1.symmetric_difference(set2))
