# Lesson 7 - Functions
# Title: Reusable code with functions
# Subtitle: Learn how functions make code organized and reusable.

# Student note:
# - Functions group code into small blocks.
# - Use return to send back a value.
# - Functions can accept parameters and return results.

print("=== Lesson 7 Classwork ===")

# Example 1: Simple function
def square(value):
    return value * value

print("Square:", square(4))

# Example 2: Function with two parameters
def add(a, b):
    return a + b

print("Sum:", add(3, 5))
print()

# Example 3: Function that uses a loop inside
# Solution:
def sum_range(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total

print("Range sum:", sum_range(2, 6))
print()

# Practice 1: Create a function that returns the area of a rectangle
# Solution:
def rectangle_area(width, height):
    return width * height

print("Practice 1:", rectangle_area(4, 6))
print()

# Practice 2: Create a function that checks if a number is even
# Solution:
def is_even(number):
    return number % 2 == 0

print("Practice 2:", is_even(8))
print()

# Practice 3: Create a function that returns the average of a list
# Solution:
def average(nums):
    return sum(nums) / len(nums)

print("Practice 3:", average([10, 20, 30]))
print()

# Challenge: Create a function that returns the factorial of a number.
# Solution:
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print("Challenge:", factorial(5))
