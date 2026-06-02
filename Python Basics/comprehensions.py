"""
Comprehensions in Python provide a concise way to create lists, dictionaries, sets, and generators. 
They allow you to generate new sequences by applying an expression to each item in an iterable, 
optionally filtering items using a condition.
"""


# List comprehension
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Dictionary comprehension
squared_dict = {x: x**2 for x in range(10)}
print(squared_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# Set comprehension
squared_set = {x**2 for x in range(10)}
print(squared_set)  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Generator expression
squared_gen = (x**2 for x in range(10))
print(squared_gen)  # Output: <generator object <genexpr> at 0x7f8b8c8c8c8c>
print(list(squared_gen))  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

