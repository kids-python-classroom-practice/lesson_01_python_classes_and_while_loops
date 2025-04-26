# Variables and Data Types - Interactive Quiz Lesson

import time

# Function to pause between sections
def pause(x=1):
    time.sleep(x)

# Function to check data type
def check_type(value, expected_type):
    return isinstance(value, expected_type)

# Function to get type description
def type_description(python_type):
    descriptions = {
        'int': "An integer is a whole number without any decimal points. Integers can be positive, negative, or zero. They are commonly used to count things, represent scores in games, or measure whole quantities like age or number of students.",
        'float': "A float is a number that has a decimal point. Floats allow for much greater precision than integers, making them useful for measurements like height, temperature, or speed. Floats can also be positive or negative.",
        'str': "A string is a sequence of characters enclosed in quotes. Strings are used to represent text such as names, sentences, or any data that consists of letters, numbers, and symbols. In Python, both single and double quotes can be used for strings.",
        'bool': "A boolean is a data type with only two possible values: True or False. Booleans are essential for controlling the flow of a program, making decisions, and performing logical operations based on conditions.",
        'list': "A list is an ordered collection of items that can be changed (mutable). Lists can hold a mix of different data types like numbers, strings, or even other lists. Items are enclosed in square brackets and separated by commas.",
        'tuple': "A tuple is similar to a list but is immutable, meaning once it is created, it cannot be modified. Tuples are useful when you want to store a fixed collection of items, like the coordinates of a point (x, y).",
        'dict': "A dictionary is a collection of key-value pairs, where each key is linked to a specific value. Dictionaries are incredibly useful for storing and organizing data, such as a person's profile or a configuration file. Keys must be unique within a dictionary.",
        'set': "A set is an unordered collection of unique items. Sets automatically remove duplicates and are useful when you want to know which items exist without worrying about their order. Sets are created using curly braces {}."
    }
    return descriptions.get(python_type, "A special or custom type.")

# Introduction
print("Welcome to the Python Variables and Data Types Lesson!")
pause()

# Step 1: Introduce Variables
print("\n🧠 What is a Variable?")
print("A variable is a container for storing data values. You assign a value using the '=' operator.")
pause()

# User creates a variable
user_input = input("\nType anything you want and we'll figure out what data type it is: ")

# Try to guess type
try:
    evaluated_input = eval(user_input)
except:
    evaluated_input = user_input

data_type = type(evaluated_input).__name__

print(f"✅ Your input '{evaluated_input}' is of type: {data_type}")
print("Description:", type_description(data_type))
print()
print("You can use variables to store data and perform operations on them.")
print("For example, you can store a number in a variable and then add it to another number.")
pause(3)
print("Let's explore different data types in Python!")
pause()

# Step 2: Cover Major Data Types

# Function for teaching a type
def teach_type(type_name, expected_type, examples, example_summary):
    print(f"\n🔹 Data Type: {type_name}")
    for line in examples:
        print("-", line)
    pause()

    # Ask user for matching input
    while True:
        user_answer = input(f"\nNow type an example of a {type_name}: ")
        try:
            evaluated = eval(user_answer)
        except:
            evaluated = user_answer  # treat as string if eval fails

        if check_type(evaluated, expected_type):
            print(f"✅ Correct! {evaluated} is a {type_name}!")
            break
        else:
            wrong_type = type(evaluated).__name__
            print(f"❌ That's not a {type_name}. You entered a {wrong_type}. Try again!")
            print(f"Reminder: A correct {type_name} might look like: {example_summary}")
            pause()

# Teach int
teach_type("Integer (int)", int, [
    "Whole numbers: positive or negative, no decimals. Examples: 1, -7, 0, 42",
    "Whole numbers are used for counting, indexing, and more.",
    "Integers are the most basic numeric data type in programming."
], "Example: 42")

# Teach float
teach_type("Float", float, [
    "Decimal numbers: include a point. Examples: 3.14, -0.001, 2.0",
    "Floats are used for precise measurements, calculations, and scientific data.",
    "Floats represent real numbers and are used across many fields from finance to physics."
], "Example: 3.14")

# Teach string
teach_type("String (str)", str, [
    "Text enclosed in quotes. Examples: 'hello', '123', 'Python is fun!'",
    "Strings can include letters, numbers, and symbols.",
    "Strings are used for user input, text processing, web development, and much more.",
    "They are the only data type that can pass unique combinations of characters like passwords or text messages."
], "Example: 'Hello world'")

# Teach boolean
teach_type("Boolean (bool)", bool, [
    "Only two values: True or False. Used in decisions.",
    "Booleans are used in conditions, loops, and logical operations.",
    "They are critical for controlling the flow of a program, enabling things like 'if this, then that' decisions."
], "Example: True")

# Teach list
teach_type("List", list, [
    "Ordered, changeable collection. Examples: [1, 2, 3], ['apple', 'banana', 'cherry']",
    "Lists can hold different data types in one collection.",
    "Lists are mutable, making it easy to add, remove, or update items.",
    "Lists are essential for managing multiple items in a single structure, like inventories, to-do lists, or playlists."
], "Example: [1, 2, 3]")

# Teach tuple
teach_type("Tuple", tuple, [
    "Ordered, unchangeable collection. Example: (1, 2, 3)",
    "Tuples are used for fixed collections of items where order matters but mutability is not needed.",
    "Common uses include storing coordinates, RGB color values, or dates (year, month, day)."
], "Example: (1, 2, 3)")

# Teach dictionary
teach_type("Dictionary (dict)", dict, [
    "Collection of key-value pairs. Example: {'name': 'Alex', 'age': 10}",
    "Keys are unique and used to access values.",
    "Dictionaries are mutable and used for structured data like profiles, settings, or mappings."
], "Example: {'name': 'Alex', 'age': 10}")

# Teach set
teach_type("Set", set, [
    "Unordered, unique items. Example: {1, 2, 3}",
    "Sets automatically remove duplicates.",
    "They are useful for membership tests, uniqueness enforcement, and set operations like union and intersection."
], "Example: {1, 2, 3}")

# Final Summary
print("\n🎉 Great job!")
print("You learned:")
print("- How variables store information")
print("- How to identify and create different Python data types")
print("- How to validate data types in Python")
pause(2)
print("\See you in the next lesson soon!")
pause(10)