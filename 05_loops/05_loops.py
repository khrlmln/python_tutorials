# ++++++++++ Loop in Python ++++++++++

# Loops are used to iterate over a sequence (like a list, tuple, string, or range) or execute a block of code multiple times.

# ++++++++++ 1. For Loop: The for loop in Python is a control flow statement used to iterate over a sequence (such as a list, tuple, dictionary, string, or range) or other iterable objects. It is one of the most commonly used constructs in Python for repetitive tasks. The for loop retrieves each item from the iterable one at a time and assigns it to the variable. The loop runs until all items in the iterable are processed.

# using range() function: The range() function generates a sequence of numbers, which is often used in loops.
for i in range(1, 6):
    print(f"{i}. Hello using for loop")

# Customizing range()
for i in range(1, 10, 2):  # Start at 1, end at 10 (exclusive), step by 2
    print(i)

# Looping through a List
my_list = ["Apple", "Mango", "Banana", "Jackfruit"]

for items in my_list:
    print(items)

# Looping through a String
for i in "Hello":
    print(i)

# Iterating through a Dictionary
my_dict = {"name": "Milan", "age": 25, "Address": "Kathmandu"}

for key, value in my_dict.items():
    print(f"{key}: {value}")

# The else Clause in a for Loop: The else block in a for loop executes if the loop completes without encountering a break statement.
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 0:
        break
else:
    print("Zero not found in numbers")

# Nested for Loops: A for loop inside another for loop is known as a nested loop.
# Input: Number of rows
rows = 3

# Outer loop for rows
for i in range(1, rows + 1):
    # Inner loop for numbers in each row
    for j in range(1, i + 1):
        print(j, end=" ")  # Print numbers in the same row with a space
    print()  # Move to the next row

# ++++++++++ 1. While Loop: A while loop in Python allows you to execute a block of code repeatedly as long as a specified condition is True.

# writing a while loop
# Initialize the variable 'count' to start at 1
count = 1

# Use a while loop to execute as long as 'count' is less than or equal to 5
while count <= 5:
    # Print the current value of 'count'
    print(count)
    # Increment 'count' by 1 to avoid an infinite loop
    count += 1

# Using a Break Statement: We can use break to exit a loop prematurely.

# Initialize the variable 'number' to start at 1
number = 1

# Use a while loop to iterate as long as 'number' is less than or equal to 10
while number <= 10:
    # Check if 'number' is equal to 7
    if number == 7:
        # Exit the loop if 'number' is 7
        break
    # Print the current value of 'number'
    print(number)
    # Increment 'number' by 1 to progress the loop
    number += 1

# Using a Continue Statement: We can use continue to skip the rest of the loop's body for the current iteration
# Initialize the variable 'number' to start at 1
number = 1

# Use a while loop to iterate as long as 'number' is less than or equal to 10
while number <= 10:
    # Check if 'number' is equal to 7
    if number == 7:
        # Skip the rest of the loop and proceed with the next iteration
        number += 1
        continue
    # Print the current value of 'number'
    print(number)
    # Increment 'number' by 1 to progress the loop
    number += 1

# Nested while loop: A nested while loop in Python refers to having one while loop inside another. This is often used for working with multi-dimensional data or scenarios that require iterating through multiple levels.

# Input: Number of rows to generate in the pattern
rows = 3

# Outer loop for iterating through each row
i = 1
while i <= rows:
    # Inner loop for printing numbers in the current row
    j = 1
    while j <= i:
        print(j, end=" ")  # Print each number in the row, separated by a space
        j += 1  # Increment the number to be printed next
    print()  # Print a newline after finishing the current row
    i += 1  # Move to the next row
