# Map is a built-in function in Python that applies a given function to each item of an 
# iterable (like a list) and returns an iterator.

x = [1, 2, 3, 4, 5]
squared = map(lambda i: i**2, x)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# Filter is a built-in function in Python that constructs an iterator 
# from elements of an iterable for which a function returns true.

x = [1, 2, 3, 4, 5]
even_numbers = filter(lambda i: i % 2 == 0, x)
print(list(even_numbers))  # Output: [2, 4]