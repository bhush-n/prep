# Sets are unordered collections of unique elements. They are defined using curly braces {} or the set() constructor.
# Sets do not allow duplicate elements and are mutable, meaning you can add or remove elements after the set is created.

# Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()
    
# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}


# Set operations

# Adding an element to a set
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing an element from a set
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5, 6}

# Checking if an element is in a set
print(4 in my_set)  # Output: True  
print(3 in my_set)  # Output: False

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union of sets
union_set = set_a.union(set_b)
print(union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection of sets
intersection_set = set_a.intersection(set_b)
print(intersection_set)  # Output: {3}

# Difference of sets
difference_set = set_a.difference(set_b)
print(difference_set)  # Output: {1, 2}

# Symmetric difference of sets
symmetric_difference_set = set_a.symmetric_difference(set_b)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}
