# Lesson 10 - Classes and Objects
# Title: Object-oriented programming basics
# Subtitle: Learn how to create classes and instances.

# Student note:
# - A class describes an object type.
# - An object is an instance of a class.
# - Methods define behavior, and attributes store data.

print("=== Lesson 10 Classwork ===")

# Example 1: Create a simple class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def describe(self):
        return f"{self.name} is {self.age} years old"

my_dog = Dog("Buddy", 3)
print(my_dog.bark())
print(my_dog.describe())
print()

# Example 2: Create a BankAccount class
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        return "Insufficient funds"

account = BankAccount("Aram", 100)
print(account.deposit(50))
print(account.withdraw(80))
print()

# Practice 1: Create a Student class
# Solution:
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_passing(self):
        return self.grade >= 50

student = Student("Maro", 80)
print("Practice 1:", student.name, student.is_passing())
print()

# Practice 2: Create a Rectangle class
# Solution:
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

print("Practice 2:", Rectangle(4, 5).area())
