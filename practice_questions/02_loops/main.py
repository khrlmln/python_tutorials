# Q.1 Given a list of numbers, count how many are positive. numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]

positive_number_count = 0

for number in numbers:
    if number > 0:
        positive_number_count += 1

print(f"positive numbers count is {positive_number_count}")

# Q.2 Calculate the sum of even numbers up to a given number n.

number = 10
sum_even = 0

for num in range(1, number + 1):
    if num % 2 == 0:
        sum_even += num

print(f"sum of even number up to {number} is {sum_even} ")

# Q.3 Print the multiplication table for a given number up to 10, but skip the fifth iteration.

num = 9

for i in range(1, 11):
    if i == 5:
        continue
    print(f"{num} x {i} = {num * i}")

# Q.4 Reverse a string using a loop.

string = "milan"
reversed_string = ""

for char in string:
    reversed_string = char + reversed_string

print(f"reversed string of {string} is {reversed_string}")

# Q.5 Given a string, find the first non-repeated character.

string = "python programming"

non_repeated_str = ""

for char in string:
    if string.count(char) == 1:
        print(f"first non-repeated character is {char}")
        break

# Q.6 Compute the factorial of a number using a while loop.

number = 10
factorial = 1

while number > 0:
    factorial *= number
    number -= 1

print(f"factorial is {factorial}")

# Q.7 Keep asking the user for input until they enter a number between 1 and 10.

while True:
    number = int(input("Enter a number between 1 and 10: "))

    if 1 <= number <= 10:
        print("number you've entered matches input condition")
        break

# Q.8 Check if a number is prime.

number = int(input("Enter a number: "))
is_prime = True

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

print(f"number {number} is a prime number: {is_prime}")

# Q.9 Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate. items = ["apple", "banana", "orange", "apple", "mango"]

items = ["apple", "banana", "orange", "apple", "mango"]
unique_item = set()

for item in items:
    if item in unique_item:
        print(f"duplicate item found: {item} ")
        break
    unique_item.add(item)

# Q.10 Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time

wait_time = 1
max_retries = 5
attempts = 1

while attempts <= max_retries:
    print(f"attempt {attempts}, wait time {wait_time}s")
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
