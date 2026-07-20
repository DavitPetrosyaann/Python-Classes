# Lesson 5 - Conditionals
# Title: Making decisions in Python
# Subtitle: Learn how if, elif, and else control program flow.

# Student note:
# - Conditions are checked with comparison operators.
# - Use if to run code when a condition is true.
# - Complex decisions often require several branches.

print("=== Lesson 5 Classwork ===")

# Example 1: Simple if/else
age = 18
if age >= 18:
    print("Adult")
else:
    print("Child")

# Example 2: Multiple conditions
grade = 85
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
else:
    print("C or lower")

# Example 3: Nested conditions
number = 12
if number > 0:
    if number % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Non-positive number")
print()

# Practice 1: Check if a number is positive, negative, or zero
# Solution:
def sign(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print("Practice 1:", sign(7))
print()

# Practice 2: Decide if a student passes a course
# Solution:
def passed(score):
    return score >= 50

print("Practice 2:", passed(60))
print()

# Practice 3: Check if a year is a leap year
# Solution:
def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0

print("Practice 3:", is_leap_year(2024))
print()

# Practice 4: Determine the ticket price category
# Solution:
def ticket_category(age):
    if age < 5:
        return "Free"
    elif age < 18:
        return "Child"
    elif age < 65:
        return "Adult"
    else:
        return "Senior"

print("Practice 4:", ticket_category(70))
