# ++++++++++ List in Python ++++++++++

# A list is a built-in data type used to store an ordered collection of items. Lists are mutable, meaning we can modify their content after creation. Lists can hold different data types, including numbers, strings, other lists, or objects.

# ++++++++++ Empty list
my_list = []

# ++++++++++ List can hold multiple data types
my_lists = [14, "Milan", None, [41, 78, "KTM"], True]

# ++++++++++ Print all values hold by list
print(f"Print all values hold by list = {my_lists}")

# ++++++++++ We've to use indexing to access specific elements. Lists are zero-indexed (start at 0).
print(f"accessing value of 3rd index = {my_lists[3]}")

# ++++++++++ Checking Membership: Use the in or not in operators to check if an item exists in a list.
print(f"'Milan' not in my_lists = {"Milan" not in my_lists}")
print(f"'Milan' in my_lists = {"Milan" in my_lists}")

# ++++++++++ Slicing lists
print(f"slicing lists from 1:3 index = {my_lists[1:3]}")

# ++++++++++ Modifying lists
my_lists[0] = 147
print(f"modifing list in '0' index = {my_lists}")

# ++++++++++ Adding elements inside a list
my_lists.append(74)  # adds to end
print(f"Adding elements to the end of a list = {my_lists}")

my_lists.insert(1, "Milan kharel")
print(f"Inserts at index 1 = {my_lists}")  # Inserts at index 1

# ++++++++++ Removing elements inside a list
my_lists.remove(74)  # Removes first occurrence of 74
print(f"Removes first occurrence of 74 = {my_lists}")

my_lists.pop(2)  # Removes element at index 2
print(f"Removes element at index 2 = {my_lists}")

# ++++++++++ Sorting elements inside a list
l = [78, 10, 960]
l.sort()  # sorts in ascending order
print(f"sorts in ascending order = {l}")

l.sort(reverse=True)  # sorts in descending order
print(f"sorts in descending order = {l}")

# ++++++++++ Reversing a list
lst = ["Milan", "Roshan", "Sneha"]

lst.reverse()
print(f"Reversing a list = {lst}")

# ++++++++++ Combining a lists
list1 = [41, "Milan", True]
list2 = [74, "Rohan", False]

# Using + operator
combined_list = list1 + list2
print(f"combining a list1 and list2 (Using + operator) = {combined_list}")

# Using extend() method
list1.extend(list2)
print(f"combining a list1 and list2 (Using extend() method) = {list1}")

# ++++++++++ Copying a List
original_list = [[41, "Milan", True], [74, "Rohan", False]]
print(f"original list {original_list}")

# Shallow copy
copy_list = original_list.copy()  # it has a same items as original_list
print(f"copy list {copy_list}")

# Deep copy
import copy

deep_copy = copy.deepcopy(original_list)

print(f"deep copy {deep_copy}")

# ++++++++++ Tuple in Python ++++++++++

# A tuple is an immutable, ordered collection of elements. Tuples are similar to lists but have one key difference: tuples cannot be modified (immutable), whereas lists can.

# ++++++++++ Empty tuple
empty_tuple = ()

# ++++++++++ Tuple with single value
single_val_tuple = (10,)

# ++++++++++ Tuple can hold multiple data types
my_tuple = (14, "Milan", None, [41, 78, "KTM"], True, (41, 78, False))

print(f"Print all values hold on tuple = {my_tuple}")

# ++++++++++ Access an element by index
print(f"accessing a value of tuple stored in 4th index = {my_tuple[3]}")

# ++++++++++ Negative indexing
print(f"Negative indexing value of my_tuple = {my_tuple[-1]}")

# ++++++++++ Slicing
print(f"slicing from 1:3 of my_tuple = {my_tuple[1:4]}")

# ++++++++++ Tuple Methods ++++++++++

# ++++++++++ Tuples have a limited set of methods due to their immutability.

# count(x)	Returns the number of occurrences of x.
print(my_tuple.count(14))

# index(x)	Returns the index of the first occurrence of x.
print(my_tuple.index(14))

# ++++++++++ Immutability of Tuples ++++++++++

# ++++++++++ Tuples cannot be modified after creation.

# Attempting to change an element
# my_tuple[0] = "Milan"  # TypeError: 'tuple' object does not support item assignment

# ++++++++++ Tuple Packing and Unpacking ++++++++++

# ++++++++++ Tuple Packing: We can "pack" values into a tuple:
packed_tuple = 1, 2, 24
print(packed_tuple)

# ++++++++++ Tuple Unpacking: We can "unpack" tuple elements into variables:
another_tuple = (41, 8, 85)

# unpacking tuple elements into variables (a, b & c)
a, b, c = another_tuple

# printing a value of variables
print(f"value of a = {a}, b = {b} and c = {c}")
