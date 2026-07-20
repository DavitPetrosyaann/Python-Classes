# Lesson 11 - Modules and Imports
# Title: Reusing code from modules
# Subtitle: Learn how to import and use Python modules.

# Student note:
# - Modules store useful functions and constants.
# - import allows us to use them.
# - Standard library modules make many tasks easier.

print("=== Lesson 11 Classwork ===")

# Example 1: Import math
import math
print("Square root of 25:", math.sqrt(25))
print("Pi:", math.pi)
print("Floor of 7.8:", math.floor(7.8))
print()

# Example 2: Import random
import random
print("Random number:", random.randint(1, 10))
print("Random choice:", random.choice(["A", "B", "C"]))
print()

# Example 3: Import datetime
from datetime import datetime
print("Current time:", datetime.now())
print()

# Practice 1: Use math to calculate the area of a circle
# Solution:
def circle_area(radius):
    return math.pi * radius * radius

print("Practice 1:", circle_area(3))
print()

# Practice 2: Pick a random item from a list
# Solution:
def pick_random(items):
    return random.choice(items)

print("Practice 2:", pick_random(["apple", "banana", "orange"]))
