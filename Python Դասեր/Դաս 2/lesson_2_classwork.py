# Lesson 2 - Strings and Lists
# Title: Built-in objects and sequences
# Subtitle: Learn how strings and lists store and organize data.

# Student note:
# - Strings are ordered collections of characters.
# - Lists store many values in one variable.
# - Indexing and slicing help us access parts of them.

print("=== Lesson 2 Classwork ===")

# Example 1: String operations
text = "Python"
print("First letter:", text[0])
print("Last letter:", text[-1])
print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Concatenation:", text + " is fun")

# Example 2: Slicing
word = "Hello World"
print("First 5 letters:", word[:5])
print("From 6 onward:", word[6:])
print("Reversed:", word[::-1])

# Example 3: List operations
numbers = [10, 20, 30, 40]
numbers.append(50)
print("After append:", numbers)

numbers.remove(20)
print("After remove:", numbers)

numbers.sort()
print("Sorted list:", numbers)

# Practice 1: Reverse a string
# Solution:
def reverse_string(s):
    return s[::-1]

print("Reverse of 'Python':", reverse_string("Python"))

# Practice 2: Count vowels
# Solution:
def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for ch in text.lower() if ch in vowels)

print("Vowels in 'Python':", count_vowels("Python"))

# Practice 3: Add an item to a list
# Solution:
def add_item(my_list, item):
    my_list.append(item)
    return my_list

print("Updated list:", add_item([1, 2, 3], 4))
