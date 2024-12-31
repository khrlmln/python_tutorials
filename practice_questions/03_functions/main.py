# Q.1 Write a function to calculate and return the square of a number.
def calculate_square(num):
    return num**2


print(calculate_square(10))


# Q.2 Create a function that takes two numbers as parameters and returns their sum.
def sum_nums(number1, number2):
    return number1 + number2


print(sum_nums(10, 45))


# Q.3 Write a function multiply that multiplies two numbers, but can also accept and multiply strings.
def multiply(number1, number2):
    return number1 * number2


print(multiply(5, 10))
print(multiply("milan", 2))

# Q.4 Create a function that returns both the area and circumference of a circle given its radius.
import math


def circle_stats(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return area, circumference


area, circumference = circle_stats(5)

print(f"area of a circle is {area:.2f}")
print(f"circumference of a circle is {circumference:.2f}")


# Q.5 Write a function that greets a user. If no name is provided, it should greet with a default name.
def greet(name="Guest"):
    return f"Hello {name}"


print(greet())
print(greet("Milan"))

# Q.6 Create a lambda function to compute the cube of a number.
cube = lambda num: num**3

print(cube(3))


# Q.7 Write a function that takes variable number of arguments and returns their sum.
def sum_of_numbers(*args):
    return sum(args)


print(sum_of_numbers(10, 20, 30))


# Q.8 Create a function that accepts any number of keyword arguments and prints them in the format key: value.
def keyword_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


keyword_args(name="Milan Kharel", email="milan@example.com")


# Q.9 Write a generator function that yields even numbers up to a specified limit.
def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i


for num in even_generator(10):
    print(num)


# Q.10 Create a recursive function to calculate the factorial of a number.
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(10))
