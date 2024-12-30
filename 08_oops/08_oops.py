# ++++++++++ Object-Oriented Programming (OOP) in Python ++++++++++

# Object-Oriented Programming (OOP) is a programming paradigm that uses "objects" to model real-world entities and their interactions. Python is an object-oriented language, and understanding OOP in Python involves knowing how to define and use classes and objects, along with concepts like inheritance, encapsulation, and polymorphism. Here are the key concepts of OOP in Python:

# ++++++++++ 1. Classes and Objects
"""
-> Class: A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.

-> Object: An instance of a class. It contains data (attributes) and methods to manipulate that data.
"""


# Defining the Student class
class Student:
    college_name = "ABC College"

    # The constructor method initializes the attributes of the student
    def __init__(self, name, age, roll_no):
        # Initializing instance variables for name, age and roll_no
        self.name = name
        self.age = age
        self.roll_no = roll_no

    # Method to display the student's information
    def display_student_info(self):
        print(
            f"Student name is: {self.name}, age is: {self.age} and roll number is: {self.roll_no}"
        )


# Creating an instance (object) of the Student class
s1 = Student("Milan kharel", 25, 5)
print(s1.college_name)

# Calling the display_student_info method on the s1 object
s1.display_student_info()


# Static Methods:
"""
    @staticmethod is a decorator that defines a method as a static method within a class. A static method is a method that belongs to the class rather than to any specific instance of the class. Unlike instance methods, a static method does not require a reference to an instance (self) or the class itself (cls) as its first parameter.

    Static methods are used when you want to define a function within a class that does not access or modify the state of the class or its instances. They are often used for utility functions that perform tasks related to the class but do not need to access class-specific data.
"""


class Vehicle:
    @staticmethod
    def greet():
        print("Hello using @staticmethod")


v1 = Vehicle()
v1.greet()


# Class Methods: The @classmethod decorator in Python is used to define a method that is bound to the class and not the instance of the class. This method receives the class as the first argument, which is typically named cls. This allows the method to access class attributes and other class methods.


class Person:
    # Class attribute, shared by all instances
    name = "anonymous"

    @classmethod
    def change_name(cls, name):
        # This method changes the class attribute 'name' for all instances
        cls.name = name


# Creating an instance of the Person class
p1 = Person()

# Calling the class method to change the class attribute 'name'
p1.change_name("Milan Kharel")

# Printing the name attribute from the instance (which accesses the class attribute)
print(p1.name)

# Printing the class attribute directly from the class
print(Person.name)


# Property Decorator: The @property decorator in Python is used to define a method as a property, allowing you to access it like an attribute while still providing the ability to use getter, setter, and deleter methods for managing the underlying data. This is particularly useful for encapsulating and controlling access to instance attributes.


class MyStudent:
    def __init__(self, physics, chemistry, math):
        # Initialize the instance variables with the provided arguments
        self.physics = physics
        self.chemistry = chemistry
        self.math = math

    @property
    def calc_percentage(self):
        # Calculate the average of the three subjects and return it as a string with a percentage sign
        return str((self.physics + self.chemistry + self.math) / 3) + "%"


# Create an instance of MyStudent with given marks for physics, chemistry, and math
student1 = MyStudent(74, 85, 96)

# Print the percentage calculated by the calc_percentage property
print(student1.calc_percentage)

# Update the physics marks for student1
student1.physics = 86

# Print the updated percentage calculated by the calc_percentage property
print(student1.calc_percentage)


# del Keyword: The del keyword in Python is used to delete objects. It can be used to delete variables, elements from lists, key-value pairs from dictionaries, or even to delete attributes from objects.


class Students:
    def __init__(self, name):
        self.name = name


student = Students("Milan Kharel")

del student  # deleted


# ++++++++++ 2. Inheritance: Inheritance allows a class to inherit attributes and methods from another class, promoting code reuse.


# Parent class
class Car:
    def __init__(self, brand, model, fuel):
        self.brand = brand
        self.model = model
        self.fuel = fuel


# Child class that inherits from Car
class ElectricVehicle(Car):
    def __init__(self, brand, model):
        # Call the parent class constructor with "Electric" as fuel type
        super().__init__(brand, model, "Electric")


# Create an instance of the Car class
c1 = Car("Toyota", "Corolla", "Diesel or Petrol")
print(f"Brand name: {c1.brand}, Model: {c1.model}, Fuel type: {c1.fuel}")

# Create an instance of the ElectricVehicle class
c2 = ElectricVehicle("Tesla", "Model Y")
print(f"Brand name: {c2.brand}, Model: {c2.model}, Fuel type: {c2.fuel}")


# ++++++++++ 3. Encapsulation: Encapsulation restricts direct access to some of an object's components, which can prevent the accidental modification of data. This is typically done by using private attributes.


class Employee:
    def __init__(self, name, salary, designation):
        self.name = name
        self.__salary = salary  # Private attribute for salary
        self.designation = designation

    def get_salary(self):
        # Returns the salary of employee
        return self.__salary


e1 = Employee("Milan Kharel", 1050000, "Software Developer")
print(
    f"Employee name is {e1.name}, salary is {e1.get_salary()} and designation is {e1.designation}"
)


# ++++++++++ 4. Polymorphism: Polymorphism allows different classes to be treated as instances of the same class through a common interface. This is usually achieved by method overriding.


# Define a class to represent complex numbers
class ComplexNumbers:
    # Constructor to initialize the real and imaginary parts of the complex number
    def __init__(self, real_num, imaginary_num):
        self.real_num = real_num
        self.imaginary_num = imaginary_num

    # Method to display the complex number in a readable format
    def show_numbers(self):
        return f"{self.real_num}i + {self.imaginary_num}j"

    # Overloading the addition operator to add two complex numbers
    def __add__(self, other):
        new_real_num = self.real_num + other.real_num
        new_imaginary_num = self.imaginary_num + other.imaginary_num
        return ComplexNumbers(new_real_num, new_imaginary_num)


# Create the first complex number object
number1 = ComplexNumbers(10, 14)
print(number1.show_numbers())

# Create the second complex number object
number2 = ComplexNumbers(15, 63)
print(number2.show_numbers())

# Add the two complex numbers and print the result
sum_numbers = number1 + number2
print(sum_numbers.show_numbers())

# Another example of implementation of polymorphism through operator overloading. Specifically, it overloads the > (greater than) operator to compare the prices of two Order objects.


# Define a class to represent an order
class Order:
    # Constructor to initialize the item and price of the order
    def __init__(self, item, price):
        self.item = item
        self.price = price

    # Overload the greater than (>) operator to compare order prices
    def __gt__(self, order2):
        return self.price > order2.price


# Create two Order objects
order = Order("Chips", 50)
order2 = Order("Eggs", 41)

# Compare the two orders using the > operator
print(order > order2)


# ++++++++++ 5. Abstraction: Abstraction hides the complex implementation details and shows only the essential features of the object. This can be achieved using abstract base classes (ABC) in Python.

from abc import ABC, abstractmethod
import math


# Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# Concrete class for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Concrete class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Create instances of the concrete classes
rectangle = Rectangle(10, 5)
print(f"Rectangle Area: {rectangle.area()}")
print(f"Rectangle Perimeter: {rectangle.perimeter()}")

circle = Circle(7)
print(f"Circle Area: {circle.area()}")
print(f"Circle Perimeter: {circle.perimeter()}")
