# Lesson 6 - Loops
# Title: Repetition with loops
# Subtitle: Learn for-loops and while-loops.

# Student note:
# - Loops help repeat actions many times.
# - for loops are good when the number of repetitions is known.
# - while loops are useful when the stopping condition is based on logic.

print("=== Lesson 6 Classwork ===")

# Example 1: for loop
for i in range(1, 6):
    print(i)

# Example 2: while loop
count = 1
while count <= 3:
    print("Count:", count)
    count += 1
print()

# Example 3: Nested loop
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
print()

# Practice 1: Print even numbers up to 10
# Solution:
def even_numbers(limit):
    result = []
    for i in range(0, limit + 1, 2):
        result.append(i)
    return result

print("Practice 1:", even_numbers(10))
print()

# Practice 2: Sum numbers from 1 to 5
# Solution:
def sum_upto(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print("Practice 2:", sum_upto(5))
print()

# Practice 3: Count how many times a value appears in a list
# Solution:
def count_occurrences(items, target):
    count = 0
    for item in items:
        if item == target:
            count += 1
    return count

print("Practice 3:", count_occurrences([2, 4, 2, 6, 2], 2))
print()

# Practice 4: Build a multiplication table for a number
# Solution:
def multiplication_table(number):
    table = []
    for i in range(1, 11):
        table.append(number * i)
    return table

print("Practice 4:", multiplication_table(7))
