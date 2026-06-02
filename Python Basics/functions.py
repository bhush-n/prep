# Functions in Python

# A function is a reusable block of code that performs a specific task.
# Functions help to break our program into smaller and modular chunks, making it more organized and manageable

# Defining a function
def greet(name):
    """This function greets the person passed as an argument."""
    return f"Hello, {name}!"

# Calling a function
print(greet("Alice"))  # Output: Hello, Alice!

# Function with default arguments
def greet(name="World"):
    """This function greets the person passed as an argument, or 'World' if no argument is provided."""
    return f"Hello, {name}!"
print(greet())  # Output: Hello, World!

# Function with variable-length arguments
def greet(*names):
    """This function greets all the people passed as arguments."""
    return "Hello, " + ", ".join(names) + "!"

print(greet("Alice", "Bob", "Charlie"))  # Output: Hello, Alice, Bob, Charlie!

