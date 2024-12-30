# ++++++++++ String in Python ++++++++++

# A string is a sequence of characters enclosed in either single quotes (' ') or double quotes (" "). Strings are one of the most commonly used data types in Python and are immutable, meaning their contents cannot be changed once they are created.

# ++++++++++ Creating a String
string1 = "This is a String"  # using double quotes (" ")

string2 = """This is a Multiline String
used for writing multiple sentences"""

print(string1)
print(string2)

# ++++++++++ String Operations

# Concatenation (joining strings)
first_name = "Milan"
last_name = "Kharel"

full_name = (
    first_name + " " + last_name
)  # full_name variable is used to store first_name and last_name value in concatinated format

print(full_name)

# Repetition
repeted_string = "Hello World! " * 3
print(repeted_string)

# Indexing: Strings in Python are zero-indexed, meaning the first character is at index 0
my_str = "hello world"
print(my_str[3])  # prints 'l' because it's stored at 3rd index

# Slicing
print(my_str[1:4])  # 'ell' (from index 1 to 4)
print(my_str[-3:-1])  # negetive slicing

# Length
print(len("Hello World!"))  # len() method is used to find length of strings

# ++++++++++ String Methods

python_intro = "    Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.    "

greeting = "Hello World!"

# .lower() - Converts string to lowercase.
print(python_intro.lower())  # changes all words into lower case

# .upper() - Converts string to uppercase.
print(python_intro.upper())

# .strip() - Removes whitespace from the beginning and end of a string.
print(python_intro.strip())

# .replace() - Replaces a substring with another substring.
print(greeting.replace("World", "Milan"))

# .find() - Finds the first occurrence of a substring, returns the index, or -1 if not found.
print(greeting.find("Hello"))

# .split() - Splits a string into a list based on a delimiter.
print(python_intro.split(" "))

# ++++++++++ String Formatting

# format strings using f-strings (from Python 3.6+), str.format(), or % formatting

# F-strings (Recommended)
# F-strings are considered the most efficient and readable method for string formatting.
name = "Milan"
age = 25
print(f"My name is {name} and I am {age} years old.")

# str.format()
print("My name is {} and I am {} years old.".format(name, age))

# % formatting (older style):
print("My name is %s and I am %d years old." % (name, age))

# ++++++++++ Conditional Statements in Python ++++++++++

# Conditional statements in Python allows us to execute certain pieces of code based on whether a condition is true or false. They are fundamental for controlling the flow of a program.

# ++++++++++ 1. if Statement: The if statement is used to check a condition. If the condition is true, the block of code inside the if statement is executed.
age = int(input("Enter your age: "))

if age >= 18:
    print("You can apply for drivers license.")

# ++++++++++ 2. if-else Statement: The if-else statement allows you to execute one block of code if the condition is true, and another block of code if the condition is false.
age = int(input("Enter your age: "))

if age >= 18:
    print("You can apply for drivers license")
else:
    print("You're underage for getting a drivers license")

# ++++++++++ 3. if-elif-else Statement: The if-elif-else statement allows you to check multiple conditions in a sequence. If the first condition is false, it moves on to the next condition, and so on. If none of the conditions are true, the else block is executed.
age = int(input("Enter your age: "))

if age < 18:
    print("You're underage for getting a drivers license")
elif 18 <= age <= 65:
    print("You can apply for drivers license")
elif age >= 65:
    print("You're too old for getting drivers license")
else:
    print("Error Occured")

# ++++++++++ 4. Nested if Statements: We can also nest if statements inside one another. This is useful for checking multiple levels of conditions.
num1 = 10
num2 = 18

if num1 > 5:
    if num2 > 10:
        print("both conditions are true")
    else:
        print("num2 is not greater than num1")
else:
    print("num1 is not greater than 5")

# ++++++++++ 5. Conditional Expressions (Ternary Operator): Python has a shorthand way of writing conditional statements using the ternary operator, which is a one-line if-else statement.
marks = 75

result = "you've scored more than 50%" if marks > 50 else "you've scored less than 50%"
print(result)
