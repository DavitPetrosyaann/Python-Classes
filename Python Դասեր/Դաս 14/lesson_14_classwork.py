# Lesson 14 - Inheritance
# Title: Reusing classes through inheritance
# Subtitle: Learn how child classes inherit from parent classes.

# Student note:
# - Child classes reuse behavior from parent classes.
# - Override methods when you want new behavior.
# - Inheritance helps avoid repeating code.

print("=== Lesson 14 Classwork ===")

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Cat(Animal):
    def speak(self):
        return "Meow"

class Dog(Animal):
    def speak(self):
        return "Woof"

print(Cat("Milo").speak())
print(Dog("Rex").speak())
print()

# Practice 1: Create a Bird class that inherits from Animal
# Solution:
class Bird(Animal):
    def speak(self):
        return "Chirp"

print("Practice 1:", Bird("Tweety").speak())
print()

# Practice 2: Create a Vehicle and Car class
# Solution:
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        return f"Brand: {self.brand}"

class Car(Vehicle):
    def info(self):
        return f"Car brand: {self.brand}"

print("Practice 2:", Car("Toyota").info())
