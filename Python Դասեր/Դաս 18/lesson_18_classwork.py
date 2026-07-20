# Lesson 18 - Mini Project
# Title: Build a small Python project
# Subtitle: Combine what you learned into a small practical app.

# Student note:
# - Mini projects help connect different concepts.
# - Start small and test each feature.
# - Real applications usually combine loops, functions, conditionals, and data structures.

print("=== Lesson 18 Classwork ===")

# Example 1: Simple calculator
def calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "Unknown operation"

print("Calculator:", calculator(10, 5, "+"))
print("Calculator:", calculator(10, 5, "*"))
print()

# Example 2: Student grade tracker
students = {"Ani": 91, "Lilit": 74, "Mher": 83}

def grade_status(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Good"
    elif score >= 70:
        return "Average"
    return "Needs work"

for name, score in students.items():
    print(name, "->", grade_status(score))
print()

# Practice 1: Create a function that checks if a password is long enough
# Solution:
def strong_password(password):
    return len(password) >= 8

print("Practice 1:", strong_password("python123"), strong_password("abc"))
print()

# Practice 2: Create a function that counts vowels in a sentence
# Solution:
def count_vowels(sentence):
    vowels = "aeiou"
    return sum(1 for ch in sentence.lower() if ch in vowels)

print("Practice 2:", count_vowels("Python is fun"))
print()

# Challenge: Create a small menu-based calculator using input().
