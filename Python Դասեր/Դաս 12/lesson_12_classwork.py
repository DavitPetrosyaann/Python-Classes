# Lesson 12 - Files
# Title: Reading and writing files
# Subtitle: Learn how Python interacts with files on disk.

# Student note:
# - open() reads and writes files.
# - Use with open(...) to safely handle files.
# - File handling is important for saving data and logs.

print("=== Lesson 12 Classwork ===")

# Example 1: Write to a file
with open("lesson12_notes.txt", "w", encoding="utf-8") as file:
    file.write("Hello from Python class\n")
    file.write("This is lesson 12\n")

# Example 2: Read from a file
with open("lesson12_notes.txt", "r", encoding="utf-8") as file:
    print(file.read())
print()

# Example 3: Append to a file
with open("lesson12_notes.txt", "a", encoding="utf-8") as file:
    file.write("Appended line\n")

with open("lesson12_notes.txt", "r", encoding="utf-8") as file:
    print("After append:")
    print(file.read())
print()

# Practice 1: Create a file with your name
# Solution:
with open("student_name.txt", "w", encoding="utf-8") as file:
    file.write("Armen")

with open("student_name.txt", "r", encoding="utf-8") as file:
    print("Saved name:", file.read())
print()

# Practice 2: Count lines in a file
# Solution:
def count_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return len(file.readlines())

print("Practice 2:", count_lines("lesson12_notes.txt"))
