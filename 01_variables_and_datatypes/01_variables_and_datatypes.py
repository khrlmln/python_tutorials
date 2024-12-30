# ++++++++++ Variables in Python ++++++++++

# Variables are used to store data values. A variable is a name that refers to a value stored in the computer's memory. We can assign a value to a variable using the = (assignment) operator.

# ++++++++++ Creating and Assigning Variables
user_name = "Milan"  # Assigning string value
user_age = 25  # Assigning integer value
is_active = True  # Assigning boolean value

print(
    "Name is", user_name, "Age is", user_age, "user is active", is_active
)  # printing a value hold by a variable

# Python is dynamically typed, meaning we don't have to declare the type of a variable explicitly. The type of the variable is inferred based on the value assigned to it.

# ++++++++++ Variable Naming Rules
"""
-> A variable name must start with a letter (a-z, A-Z) or an underscore (_).
-> The rest of the variable name can include letters, numbers (0-9), or underscores.
-> Variable names are case-sensitive (e.g., variable and Variable are different).
-> Cannot use Python keywords or reserved words (like if, else, while, class, etc.) as variable names.
"""

# ++++++++++ Data Types in Python ++++++++++

"""
Data types define the kind of value a variable can hold. Python supports a variety of built-in data types that fall into categories like numbers, sequences, mappings, sets, and more.
-> Integers: Integer type, for whole numbers (both positive and negative) without any decimal point.
-> String: String type, used for text or a sequence of characters. Strings are enclosed in single or double quotes.
-> Float: Floating-point type, for decimal numbers.
-> Boolean: Boolean type, used for representing truth values. It can only take two values: True or False.
-> None: This type represents the absence of a value or a null value. It is often used to represent an empty or uninitialized variable.
"""

# Example:

contact = 9874125638  # Integer type
full_name = "Milan Kharel"  # String type
age = 25.00  # Floating-point type
is_logged_in = True  # Boolean type
driving_license = None  # null value

# Aditionally, we can use the type() function to get the type of an object or variable. It returns the type of the object passed to it
print(type(contact))
print(type(full_name))
print(type(age))
print(type(is_logged_in))
print(type(driving_license))

# ++++++++++ Operators in Python ++++++++++

# Operators are special symbols used to perform operations on values or variables. Python has a wide range of operators, which can be categorized into several groups based on their functionality.

# 1. Arithmetic Operators
# These operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.
"""
+ : Addition (e.g., a + b)
- : Subtraction (e.g., a - b)
* : Multiplication (e.g., a * b)
/ : Division (returns a float) (e.g., a / b)
// : Floor Division (returns an integer) (e.g., a // b)
% : Modulus (returns the remainder) (e.g., a % b)
** : Exponentiation (e.g., a ** b)
"""

# Example:

number1 = 12
number2 = 23

print(f"number1 = {number1} & number2 = {number2}")
print(f"number1 + number2 = {number1 + number2}")
print(f"number1 - number2 = {number1 - number2}")
print(f"number1 * number2 = {number1 * number2}")
print(f"number1 / number2 = {number1 / number2}")
print(f"number1 // number2 = {number1 // number2}")
print(f"number1 % number2 = {number1 % number2}")
print(f"number1^number2 = {number1**number2}")

# 2. Comparison Operators
# These operators are used to compare two values and return a boolean (True or False).
"""
== : Equal to (e.g., a == b)
!= : Not equal to (e.g., a != b)
> : Greater than (e.g., a > b)
< : Less than (e.g., a < b)
>= : Greater than or equal to (e.g., a >= b)
<= : Less than or equal to (e.g., a <= b)
"""

# Example:

print(f"number1 == number2 = {number1 == number2}")
print(f"number1 != number2 = {number1 != number2}")
print(f"number1 > number2 = {number1 > number2}")
print(f"number1 < number2 = {number1 < number2}")
print(f"number1 >= number2 = {number1 >= number2}")
print(f"number1 <= number2 = {number1 <= number2}")

# 3. Assignment Operators
# These operators are used to assign values to variables.
"""
= : Assign (e.g., a = 5)
+= : Add and assign (e.g., a += 5 is equivalent to a = a + 5)
-= : Subtract and assign (e.g., a -= 5 is equivalent to a = a - 5)
*= : Multiply and assign (e.g., a *= 5 is equivalent to a = a * 5)
/= : Divide and assign (e.g., a /= 5 is equivalent to a = a / 5)
//= : Floor divide and assign (e.g., a //= 5 is equivalent to a = a // 5)
%= : Modulus and assign (e.g., a %= 5 is equivalent to a = a % 5)
**= : Exponentiate and assign (e.g., a **= 5 is equivalent to a = a ** 5)
"""

# Example:

num = 100
num += 100
num -= 100
num *= 100
num /= 100
num //= 100
num %= 100
num **= 100

# 4. Logical Operators
# These operators are used to combine conditional statements and return a boolean value.
"""
and : Returns True if both statements are true (e.g., a and b)
or : Returns True if at least one statement is true (e.g., a or b)
not : Reverses the boolean value (e.g., not True)
"""

# Example:

# And
print(
    "number1 is greater than 10 and number2 is greater than 10:",
    (number1 > 10) and (number2 > 10),
)

# Or
print(
    "number1 is greater than 10 or number2 is greater than 10:",
    (number1 > 10) or (number2 > 10),
)

# Not
print(f"not (number1 > number2) = {not (number1 > number2)}")

# ++++++++++ Type Conversion in Python ++++++++++

# Type conversion refers to the process of converting one data type into another. This can happen automatically (implicit conversion) or manually (explicit conversion). Here’s an overview of how it works:

# 1. Implicit Type Conversion (Automatic Type Conversion)
# Python automatically converts one data type to another when necessary. This usually happens when we perform operations involving mixed data types. For example:

num_one = 5  # integer
num_two = 3.2  # float
sum = (
    num_one + num_two
)  # Python automatically converts num_one (int) to float before adding
print(f"sum of {num_one} and {num_two} = {sum}")

# 2. Explicit Type Conversion (Manual Type Conversion)
# Explicit conversion is when we manually convert one data type to another using built-in functions. These functions are also known as type casting. For example:

num1 = "42"
converted_number = int(num1)  # Converts string to integer
print(f"converted from string into int is = {converted_number}")

# ++++++++++ User Inputs in Python ++++++++++

# The input() function in Python is used to take input from the user. It reads a line of text entered by the user and returns it as a string. For example:

username = input("Enter your name: ")
userage = int(
    input("Enter your age: ")
)  # Converts string to integer because input() returns anything user written as a string

print("Your name is:", username, "and age is:", userage)
