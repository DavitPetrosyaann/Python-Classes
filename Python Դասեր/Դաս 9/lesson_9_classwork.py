# Lesson 9 - Sets and Comprehensions
# Title: Compact data processing
# Subtitle: Learn sets and list comprehensions.

# Student note:
# - Sets store unique values.
# - Comprehensions create lists quickly and clearly.
# - They are useful for compact and readable transformations.

print("=== Lesson 9 Classwork ===")

# Example 1: Create a set
numbers = {1, 2, 2, 3}
print("Set:", numbers)

# Example 2: List comprehension
squares = [x * x for x in range(1, 6)]
print("Squares:", squares)

# Example 3: Filter even numbers
evens = [x for x in range(1, 11) if x % 2 == 0]
print("Evens:", evens)
print()

# Example 4: Set comprehension from a list
words = ["apple", "banana", "apple", "grape"]
unique_words = {word for word in words}
print("Unique words:", unique_words)
print()

# Practice 1: Create a list of cubes
# Solution:
def cubes(limit):
    return [x * x * x for x in range(1, limit + 1)]

print("Practice 1:", cubes(4))
print()

# Practice 2: Create a set from a list
# Solution:
def unique_values(items):
    return set(items)

print("Practice 2:", unique_values([1, 2, 2, 3, 3]))
print()

# Practice 3: Create a list of uppercase words
# Solution:
def uppercase_words(words):
    return [word.upper() for word in words]

print("Practice 3:", uppercase_words(["python", "class", "study"]))
print()

# Challenge: Create a list of only numbers divisible by 3 from 1 to 20.
# Solution:
def divisible_by_three(limit):
    return [x for x in range(1, limit + 1) if x % 3 == 0]

print("Challenge:", divisible_by_three(20))
