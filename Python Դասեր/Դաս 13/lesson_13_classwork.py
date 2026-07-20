# Lesson 13 - Exceptions
# Title: Handling errors safely
# Subtitle: Learn how to catch and manage exceptions.

# Student note:
# - Exceptions happen when something goes wrong.
# - try/except helps your program continue.
# - Good programs handle likely errors before they crash.

print("=== Lesson 13 Classwork ===")

# Example 1: Catch invalid input
try:
    number = int("abc")
except ValueError:
    print("That is not a valid integer")

# Example 2: Handle division by zero
try:
    print(10 / 0)
except ZeroDivisionError:
    print("You cannot divide by zero")
print()

# Example 3: Handle multiple exceptions
try:
    value = int(input("Enter a number: "))
    result = 10 / value
    print("Result:", result)
except ValueError:
    print("Please enter an integer")
except ZeroDivisionError:
    print("Cannot divide by zero")
print()

# Practice 1: Convert a value safely
# Solution:
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None

print("Practice 1:", safe_int("25"), safe_int("hello"))
print()

# Practice 2: Safely access a list item
# Solution:
def safe_get(items, index):
    try:
        return items[index]
    except IndexError:
        return "Index out of range"

print("Practice 2:", safe_get([1, 2, 3], 5))
