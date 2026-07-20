# Lesson 15 - Iterators and Generators
# Title: Creating sequences lazily
# Subtitle: Learn how generators yield values one at a time.

# Student note:
# - Generators are useful for large or infinite sequences.
# - They save memory because they generate values on demand.
# - They are ideal when you do not need all values at once.

print("=== Lesson 15 Classwork ===")

# Example 1: Generator function
def count_up(limit):
    for i in range(limit):
        yield i

for value in count_up(4):
    print(value)
print()

# Example 2: Generator for even numbers
# Solution:
def even_numbers(limit):
    for i in range(0, limit + 1, 2):
        yield i

print("Even numbers:", list(even_numbers(10)))
print()

# Practice 1: Create a generator for squares
# Solution:
def squares(limit):
    for i in range(1, limit + 1):
        yield i * i

print("Practice 1:", list(squares(5)))
print()

# Practice 2: Create a generator for Fibonacci numbers
# Solution:
def fibonacci(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

print("Practice 2:", list(fibonacci(8)))
