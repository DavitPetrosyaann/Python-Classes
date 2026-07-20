# Lesson 8 - Dictionaries
# Title: Working with key-value data
# Subtitle: Learn how dictionaries store information in pairs.

# Student note:
# - Dictionaries use keys and values.
# - Keys must be unique.
# - Nested dictionaries can represent more complex information.

print("=== Lesson 8 Classwork ===")

# Example 1: Create a dictionary
student = {"name": "Anna", "age": 20, "grade": "A"}
print(student)

# Example 2: Access and update values
print(student["name"])
student["age"] = 21
print(student)
print()

# Example 3: Nested dictionary
student_profile = {
    "name": "Mher",
    "scores": {"math": 90, "science": 85},
    "active": True
}
print(student_profile)
print(student_profile["scores"]["math"])
print()

# Practice 1: Create a dictionary for a book
# Solution:
def make_book(title, author, year):
    return {"title": title, "author": author, "year": year}

print("Practice 1:", make_book("Python", "Guido", 1991))
print()

# Practice 2: Get a value by key
# Solution:
def get_value(my_dict, key):
    return my_dict.get(key, "Not found")

print("Practice 2:", get_value(student, "grade"))
print()

# Practice 3: Count the number of items in a dictionary
# Solution:
def count_items(my_dict):
    return len(my_dict)

print("Practice 3:", count_items({"a": 1, "b": 2, "c": 3}))
print()

# Practice 4: Create a dictionary from two lists
# Solution:
def combine_lists(keys, values):
    return dict(zip(keys, values))

print("Practice 4:", combine_lists(["name", "age"], ["Aram", 19]))
