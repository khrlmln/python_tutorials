# Q.1 Create a Car class with attributes like brand and model. Then create an instance of this class.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


car_one = Car("Toyota", "Corolla")

print(car_one.brand, car_one.model)


# Q.2 Add a method to the Car class that displays the full name of the car (brand and model).
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_fullname(self):
        return f"{self.brand} {self.model}"


car_one = Car("Toyota", "Corolla")

print(car_one.display_fullname())


# Q.3 Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_fullname(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


car_two = ElectricCar("Tesla", "Model Y", "100kWh")

print(f"{car_two.display_fullname()} {car_two.battery_size}")


# Q.4 Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.
class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand


car_one = Car("Toyota", "Corolla")

print(car_one.get_brand())


# Q.5 Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_fullname(self):
        return f"{self.brand} {self.model}"

    def fuel_type(self):
        return "Diesel or Petrol"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric charge"


car_one = Car("Toyota", "Hilux")
print(car_one.fuel_type())

car_two = ElectricCar("Tesla", "Model Y", "100kWh")
print(car_two.fuel_type())


# Q.6 Add a class variable to Car that keeps track of the number of cars created.
class Car:
    total_car_created = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Car.total_car_created += 1


car_one = Car("Toyota", "Corolla")
print(car_one.brand, car_one.model)

print(Car.total_car_created)


# Q.7 Add a static method to the Car class that returns a general description of a car.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @staticmethod
    def description():
        return "Hello from car class"


print(Car.description())


# Q.8 Use a property decorator in the Car class to make the model attribute read-only.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model

    @property
    def model(self):
        return self.__model


car_one = Car("Toyota", "Corolla")

# car_one.model = "Hilux"  # not working as expected

print(
    car_one.model
)  # prints a model as Corolla because model has been made read only using @property decorator


# Q.9 Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_fullname(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


my_tesla = ElectricCar("Tesla", "Model Y", "100kWh")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))


# Q.10 Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Battery:
    def battery_status(self):
        return "battery status is OK"


class Engine:
    def engine_status(self):
        return "engine status is OK"


class ElectricCar(Car, Battery, Engine):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


new_car = ElectricCar("Tata", "Nexon", "80kWh")

print(
    f"car brand: {new_car.brand}, car model: {new_car.model}, battery capacity: {new_car.battery_size}, battery status: {new_car.battery_status()}, engine status: {new_car.engine_status()}"
)
