# Lesson 1 - Variables, Printing, and Input
# Title: Getting started with Python
# Subtitle: Learn how to print output, create variables, and take input.

# Student note:
# - Use print() to show information.
# - Variables store values for later use.
# - input() lets the user enter data.

print("=== Lesson 1 Classwork ===")

# Example 1: Printing text
print("Hello, students!")

# Example 2: Variables
name = "Ani"
age = 16
print("My name is", name)
print("I am", age, "years old")
print(f"{name} is {age} years old")

# Example 3: Arithmetic
x = 10
y = 3
print("x + y =", x + y)
print("x * y =", x * y)
print("x / y =", x / y)

# Example 4: Input from the user
try:
    student_name = input("Enter your name: ")
except EOFError:
    student_name = "Student"
print("Welcome", student_name)

# Practice 1: Create two variables for your first name and favorite color.
first_name = "Armen"
favorite_color = "blue"
print("First name:", first_name)
print("Favorite color:", favorite_color)

# Practice 2: Ask for age and print the age next year.
try:
    age = int(input("Enter your age: "))
except (EOFError, ValueError):
    age = 16
print("Next year you will be", age + 1)
