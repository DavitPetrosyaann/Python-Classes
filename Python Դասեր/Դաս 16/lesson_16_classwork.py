# Lesson 16 - Decorators
# Title: Changing function behavior
# Subtitle: Learn how decorators wrap functions with extra behavior.

# Student note:
# - Decorators add functionality without changing the function body.
# - They are often used for logging, validation, and access control.
# - A decorator takes a function and returns a new function.

print("=== Lesson 16 Classwork ===")

# Example 1: Simple decorator
print("Example 1: Greeting decorator")
def greet_decorator(func):
    def wrapper():
        print("Hello from decorator")
        return func()
    return wrapper

@greet_decorator
def say_hello():
    print("Hello!")

say_hello()
print()

# Example 2: Decorator with a message
print("Example 2: Message decorator")
def message_decorator(func):
    def wrapper():
        print("Before calling the function")
        result = func()
        print("After calling the function")
        return result
    return wrapper

@message_decorator
def print_message():
    print("Function is running")

print_message()
print()

# Practice 1: Create a decorator that prints an execution message
# Solution:
def announce(func):
    def wrapper():
        print("Running function")
        return func()
    return wrapper

@announce
def show_message():
    print("Done")

show_message()
print()

# Practice 2: Create a decorator that adds a prefix to a returned string
# Solution:
def add_prefix(func):
    def wrapper():
        return "Prefix: " + func()
    return wrapper

@add_prefix
def greet():
    return "Hello"

print(greet())
print()

# Practice 3: Create a decorator that counts how many times a function is called
# Solution:
def counter(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        print(f"Called {count} times")
        return func()
    return wrapper

@counter
def greet_once():
    print("Greeting")

greet_once()
greet_once()
print()

# Challenge: Try to write your own decorator for a function that prints a name.
