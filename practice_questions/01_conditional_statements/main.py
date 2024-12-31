# Q.1  Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

age = int(input("Enter age: "))

if age <= 0:
    print("Invalid age")
elif age < 13:
    print("Child")
elif age <= 19:
    print("Teeneger")
elif age <= 59:
    print("Adult")
else:
    print("Senior")

# Q.2 Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

age = int(input("Enter age: "))
day = "wednesday"
discount = 2

price = 12 if age >= 18 else 8

if day == "wednesday":
    price -= discount

print(price)

# Q.3 Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = int(input("Enter your score: "))

if score < 0 or score > 100:
    print("please enter a valid score")
else:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"your grade is: {grade}")

# Q.4 Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

color = ("green", "yellow", "brown")
fruit_color = input("Enter a fruit color (green, yellow or brown): ")

if fruit_color not in color:
    print("Enter a valid color")
else:
    if fruit_color == "green":
        fruit_ripe = "unripe"
    elif fruit_color == "yellow":
        fruit_ripe = "ripe"
    else:
        fruit_ripe = "overripe"

    print(f"fruit is {fruit_ripe}")

# Q.5 Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather_input = input("Enter the current weather (sunny, rainy, snowy): ").lower()

if weather_input == "sunny":
    activity = "Go for a walk"
elif weather_input == "rainy":
    activity = "Read a book"
elif weather_input == "snowy":
    activity = "Build a snowman"
else:
    activity = "Sorry, I don't have a suggestion for that weather condition."

print(activity)

# Q.6 Choose a mode of transportation based on the distance (e.g., <3 km: Walk, 3-15 km: Bike, >15 km: Car).

distance = int(input("Enter a distance: "))

if distance < 3:
    transport_mode = "Walk"
elif distance <= 15:
    transport_mode = "Bike"
else:
    transport_mode = "Car"

print(f"distance: {distance} and transport mode: {transport_mode}")

# Q.7 Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = "medium"
extra_shot = True

if extra_shot:
    coffee = f"{order_size} coffee with an extra shot"
else:
    coffee = f"{order_size} coffee"

print(f"Order: {coffee}")

# Q.8 Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = "myP@ss12#word"

if len(password) < 6:
    strength = "weak"
elif len(password) <= 10:
    strength = "medium"
else:
    strength = "strong"

print(f"your password strength is `{strength}`")

# Q.9 Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year = 2008

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

# Q.10 "Write a program that recommends a type of pet food based on the pet's species and age. The recommendations are as follows:
"""
For dogs:
    If the dog is younger than 2 years old, recommend puppy food.
    If the dog is 2 years or older, recommend adult dog food.
For cats:
    If the cat is older than 5 years, recommend senior cat food.
    If the cat is 5 years old or younger, recommend adult cat food.
"""
# program should take the pet's species and age as input and print the corresponding pet food recommendation.

pet_species = input("enter pet species (cat or dog): ").lower()
pet_age = int(input("enter an age: "))

if pet_species == "dog" and pet_age < 2:
    pet_food = "puppy food"
elif pet_species == "dog" and pet_age >= 2:
    pet_food = "adult dog food"
elif pet_species == "cat" and pet_age > 5:
    pet_food = "senior cat food"
elif pet_species == "cat" and pet_age <= 5:
    pet_food = "adult cat food"
else:
    pet_food = "unknown food type"

print(pet_food)
