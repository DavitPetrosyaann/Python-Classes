# Lesson 3 - Strings and Text Processing
# Title: Working with text
# Subtitle: Learn common string methods, formatting, and manipulation.

# Student note:
# - String methods help us inspect and transform text.
# - format() and f-strings make output clearer and more readable.
# - String problems often require combining multiple operations.

print("=== Lesson 3 Classwork ===")

# Example 1: Common string methods
name = "student"
print("Capitalized:", name.capitalize())
print("Title case:", name.title())
print("Replaced:", name.replace("t", "T"))
print("Uppercase:", name.upper())
print("Length:", len(name))
print()

# Example 2: Remove extra spaces
text = "  Python   is   fun  "
print("Original:", text)
print("Trimmed:", text.strip())
print("Collapsed spaces:", " ".join(text.split()))
print()

# Example 3: String formatting
age = 20
print("Formatted with format():", "I am {} years old".format(age))
print("Formatted with f-string:", f"I am {age} years old")
print()

# Example 4: Build a full message from parts
first_name = "Lilit"
last_name = "Karapetyan"
message = "Hello " + first_name + " " + last_name + "!"
print(message)
print()

# Practice 1: Create a greeting message
# Solution:
def greet(first_name, last_name):
    return f"Hello {first_name} {last_name}!"

print("Practice 1:", greet("Lilit", "Karapetyan"))
print()

# Practice 2: Count spaces in a sentence
# Solution:
def count_spaces(sentence):
    return sentence.count(" ")

print("Practice 2:", count_spaces("Python is easy"))
print()

# Practice 3: Reverse words in a phrase
# Solution:
def reverse_words(sentence):
    words = sentence.split()
    return " ".join(reversed(words))

print("Practice 3:", reverse_words("Python is fun"))
print()

# Practice 4: Count vowels in a string
# Solution:
def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for ch in text.lower() if ch in vowels)

print("Practice 4:", count_vowels("Programming"))
print()

# Practice 5: Make the first letter of each word uppercase
# Solution:
def title_case(sentence):
    return sentence.title()

print("Practice 5:", title_case("python programming class"))
print()

# Challenge: Build a function that removes repeated spaces and capitalizes the first letter of each word.
# Solution:
def clean_title(sentence):
    words = sentence.split()
    return " ".join(word.capitalize() for word in words)

print("Challenge:", clean_title("python   is   amazing"))
