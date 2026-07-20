# Lesson 17 - Regular Expressions
# Title: Pattern matching with regex
# Subtitle: Learn how to search and extract text patterns.

# Student note:
# - regex helps find patterns in strings.
# - re.findall() finds many matches.
# - Patterns can be used to validate and extract text.

import re

print("=== Lesson 17 Classwork ===")

# Example 1: Find digits
text = "abc123def456"
print("Digits:", re.findall(r"\d+", text))

# Example 2: Find words starting with a letter
words = re.findall(r"\b[a-zA-Z]+\b", "Python 2024 class")
print("Words:", words)
print()

# Example 3: Validate email format
email = "student@example.com"
print("Email check:", bool(re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", email)))
print()

# Practice 1: Find all vowels
# Solution:
def find_vowels(text):
    return re.findall(r"[aeiouAEIOU]", text)

print("Practice 1:", find_vowels("Hello World"))
print()

# Practice 2: Extract all numbers from a sentence
# Solution:
def extract_numbers(text):
    return re.findall(r"\d+", text)

print("Practice 2:", extract_numbers("I have 2 cats and 3 dogs"))
print()

# Practice 3: Replace spaces with underscores
# Solution:
def replace_spaces(text):
    return re.sub(r"\s+", "_", text)

print("Practice 3:", replace_spaces("Python class notes"))
