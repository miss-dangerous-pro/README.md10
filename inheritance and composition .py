# inheritance 
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

dog = Dog()
print(dog.speak()) 

# Composition 
class Wheel:
    def roll(self):
        print("Wheel rolling")

class Car:
    def __init__(self):
        self.wheel = Wheel()

    def move(self):
        self.wheel.roll()
        print("Car moving")

# combining the both 
class Engine:
    def start(self):
        print("Engine started")

class Vehicle:
    def drive(self):
        print("Vehicle driving")

class Car(Vehicle):  # Inheritance
    def __init__(self):
        self.engine = Engine()  # Composition

    def start(self):
        self.engine.start()
        super().drive()

car = Car()
car.start()
# An Overview of Inheritance in Python
# The Object Super Class in  inheritance of python 

class MyClass(object): 
    def __init__(self, name):
        self.name = name

obj = MyClass("Example")
print(isinstance(obj, object)) 

# Define a base class that inherits from `object` 
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

    def __str__(self):
        return f"Animal named {self.name}"

# Define a subclass that inherits from `Animal`
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        return f"{self.name} barks"

    def __str__(self):
        return f"{super().__str__()}, Breed: {self.breed}"


my_dog = Dog("Buddy", "Golden Retriever")

print(my_dog.speak())         
print(str(my_dog))           
print(isinstance(my_dog, Dog))
print(isinstance(my_dog, Animal)) 
print(isinstance(my_dog, object)) 

# Exceptions Are an Exception
number = input("Enter a number: ")
print(f"Performing division using the number {number}:")
try:
    result = 100 / int(number)
    print(f"100 divided by {number} is {result}")
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Invalid input! Please enter a numeric value.")

print("The result has been displayed")
print("End of program")

# Creating Class Hierarchies
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def description(self):
        return f"This is a vehicle made by {self.brand}."

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def description(self):
        return f"This is a {self.model} made by {self.brand}."

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def description(self):
        return f"This is an electric {self.model} by {self.brand} with a {self.battery_capacity}kWh battery."

tesla = ElectricCar("Tesla", "Model S", 100)
print(tesla.description())

# Abstract Base Classes in Python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Circle(Shape):
    type = "Circle"

    def __init__(self, radius):
        self.radius = radius

    def printarea(self):
        return math.pi * self.radius ** 2

circle1 = Circle(5) 
print(f"The area of the circle is: {circle1.printarea():.2f}")

# Implementation Inheritance vs Interface Inheritance
# Implementation Inheritance 
class Animal:
    def eat(self):
        print("This animal eats food.")

    def sleep(self):
        print("This animal sleeps.")

class Dog(Animal):  # Reuse functionality
    def bark(self):
        print("The dog barks.")

dog = Dog()
dog.eat()   
dog.sleep() 
dog.bark()  
# Interface Inheritance
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Subclasses must implement this method."""
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print(dog.sound()) 
print(cat.sound()) 


# The Class Explosion Problem
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# More specialized classes
class ColoredRectangle(Rectangle):
    def __init__(self, length, breadth, color):
        super().__init__(length, breadth)
        self.color = color

class ColoredCircle(Circle):
    def __init__(self, radius, color):
        super().__init__(radius)
        self.color = color

# Even more specialized classes
class SmallRectangle(ColoredRectangle):
    def __init__(self, length, breadth, color, size):
        super().__init__(length, breadth, color)
        self.size = size

class SmallCircle(ColoredCircle):
    def __init__(self, radius, color, size):
        super().__init__(radius, color)
        self.size = size

# Inheriting Multiple Classes
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Bird:
    def fly(self):
        print("Bird flies")

class Eagle(Animal, Bird):
    def hunt(self):
        print("Eagle hunts")

eagle = Eagle()
eagle.speak()  
eagle.fly()   
eagle.hunt() 
# Composition in Python
# Flexible Designs With Composition

# customizing behaviour with composition in python 
class WalkBehavior:
    def move(self):
        return "I am walking"


class FlyBehavior:
    def move(self):
        return "I am flying"


class Animal:
    def __init__(self, movement):
        self.movement = movement  

    def move(self):
        return self.movement.move()


# Customizing behavior
walking_animal = Animal(WalkBehavior())
print(walking_animal.move()) 

flying_animal = Animal(FlyBehavior())
print(flying_animal.move()) 
