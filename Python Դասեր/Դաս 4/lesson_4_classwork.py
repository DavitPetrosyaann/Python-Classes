# Lesson 4 - Lists and Data Storage
# Title: Working with lists
# Subtitle: Learn how to store, access, and transform multiple values.

# Student note:
# - Lists can contain any values, even other lists.
# - append(), remove(), insert(), and sort() help us manage data.
# - Indexing and slicing are essential for working with lists.

print("=== Lesson 4 Classwork ===")

# Example 1: Create and print a list
colors = ["red", "green", "blue", "yellow"]
print("Original list:", colors)

# Example 2: Add and remove items
colors.append("orange")
print("After append:", colors)
colors.remove("green")
print("After remove:", colors)
colors.insert(1, "purple")
print("After insert:", colors)

# Example 3: Access items by index and slice
print("First item:", colors[0])
print("Last item:", colors[-1])
print("First three items:", colors[:3])
print("Every second item:", colors[::2])
print()

# Practice 1: Find the middle element
# Solution:
def middle_element(items):
    return items[len(items) // 2]

print("Practice 1:", middle_element([1, 2, 3, 4, 5]))
print()

# Practice 2: Sum a list of numbers
# Solution:
def sum_numbers(nums):
    total = 0
    for num in nums:
        total += num
    return total

print("Practice 2:", sum_numbers([2, 4, 6, 8]))
print()

# Practice 3: Remove duplicates from a list
# Solution:
def unique_items(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result

print("Practice 3:", unique_items([1, 2, 2, 3, 3, 4]))
print()

# Practice 4: Sort numbers in descending order
# Solution:
def descending(nums):
    return sorted(nums, reverse=True)

print("Practice 4:", descending([9, 1, 7, 3]))
print()

# Challenge: Create a function that returns the largest and smallest values in a list.
# Solution:
def min_max(nums):
    return min(nums), max(nums)

print("Challenge:", min_max([4, 8, 2, 10, 6]))
