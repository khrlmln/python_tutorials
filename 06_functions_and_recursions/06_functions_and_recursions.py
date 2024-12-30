# ++++++++++ Function in Python ++++++++++

# A function is a block of organized, reusable code that is used to perform a single, related action. Functions help break programs into smaller, modular chunks, improving code readability and reusability.
"""
1. Built-in Functions: These are functions that are already available in Python. They are part of the Python standard library and do not require any additional code or definition to use. We can call them directly in our program.
Examples of Built-in Functions:
    print(): Prints output to the console.
    len(): Returns the length of an object (like a list, string, etc.).
    type(): Returns the type of an object.
"""

"""
2. User-Defined Functions: These are functions that we define in our program to perform specific tasks. They allow us to group code into reusable blocks, making our program more organized and modular.
Examples of User-Defined Functions:
"""


# A Simple Function
def sum_of_numbers(num1, num2):
    sum = num1 + num2
    return sum


print(sum_of_numbers(10, 45))


# A Function with Default Parameters
def greeting(name, message="Hello"):
    response = message + " " + name  # Greets the user with a custom or default message
    return response


print(greeting("Milan"))
print(greeting("Milan", "Welcome"))


# A Function with Arbitrary Arguments


# Arbitrary positional arguments (*args):
def sums(*args):
    return sum(args)


print(sums(10, 78, 74, 96))


# Arbitrary keyword arguments (**kwargs):
def user_info(**kwargs):
    # Iterate over each key-value pair in the kwargs dictionary
    for key, value in kwargs.items():
        print(f"{key} = {value}")  # Print the key and its associated value


user_info(user_name="Milan", age=25, email="milan@example.com")

# A Function Without a Return Statement: If a function doesn’t include a return statement, it implicitly returns None


def greet(name):
    print(f"Hello {name}")  # Print the greeting message


# Call the greet function with a sample name
result = greet("Milan")

print(result)  # Since the function returns None, this will print 'None'

# ++++++++++ Recursion in Python ++++++++++

# Recursion in Python refers to the technique where a function calls itself in order to solve smaller instances of the same problem. It is a common and powerful method for solving problems that can be broken down into smaller, similar subproblems, such as in tree traversal, sorting algorithms, or mathematical calculations (e.g., factorials, Fibonacci numbers).


# basic example of recursion
def show_nums(n):
    # Base case: If n is 0, stop the recursion and return.
    # This ensures that the function does not call itself indefinitely.
    if n == 0:
        return
    # Recursive case: Print the current value of n and then call show_nums with n-1.
    # This prints numbers from n down to 1, one at a time.
    else:
        print(n)
        show_nums(n - 1)


show_nums(10)

# Basic Structure of Recursion
"""
A recursive function typically has two key components:
    1. Base case(s): This is the condition under which the recursion terminates. Without a base case, the function would continue calling itself indefinitely, leading to a stack overflow.
    2. Recursive case(s): This is where the function calls itself with a simpler version of the original problem.
"""


# Example 1: Factorial Function: A classic example of recursion is the calculation of the factorial of a number. The factorial of n (denoted as n!) is the product of all positive integers less than or equal to n.
def factorial(n):
    # Base case: when n is 0, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: multiply n by the factorial of (n-1)
    else:
        return n * factorial(n - 1)


print(f"factioral or 10 is {factorial(10)}")


# Example 2: Fibonacci Sequence: The Fibonacci sequence is another example of a problem that is often solved recursively.
def fibonacci(n):
    # Base cases
    if n == 0:
        return
    elif n == 1:
        return 1
    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))


# Example 3: Sum of Elements in a List: We can also use recursion for summing elements in a list.
def sum_of_list(lst):
    # Base case: empty list
    if not lst:
        return
    # Recursive case: first element + sum of rest of the list
    else:
        return lst[0] + sum_of_list(lst[1:])


print(sum_of_list([11, 2, 3, 4]))
