# Dictionaries are a collection of key-value pairs. They are unordered, mutable, and indexed by keys.
# Dictionaries are defined using curly braces {} with key-value pairs separated by a colon :.

# Creating an empty dictionary
empty_dict = {}

# Creating a dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}


# Accessing values in a dictionary
print(my_dict['name'])  # Output: Alice

# Adding a new key-value pair to the dictionary
my_dict['country'] = 'USA'
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}

# Removing a key-value pair from the dictionary
del my_dict['age']
print(my_dict)  # Output: {'name': 'Alice', 'city': 'New York', 'country': 'USA'}

# Checking if a key is in the dictionary
print('name' in my_dict)  # Output: True

# Iterating over a dictionary
for key, value in my_dict.items():
    print(key, value)  # Output: name Alice, city New York, country USA

# Dictionary methods

# keys() method returns a view object that displays a list of all the keys in the dictionary.
print(my_dict.keys())  # Output: dict_keys(['name', 'city', 'country'])

# values() method returns a view object that displays a list of all the values in the dictionary.
print(my_dict.values())  # Output: dict_values(['Alice', 'New York', 'USA'])

# items() method returns a view object that displays a list of dictionary's key-value tuple pairs
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('city', 'New York'), ('country', 'USA')])

# get() method returns the value for the specified key if the key is in the dictionary, else it returns None or a default value if provided.
print(my_dict.get('name'))  # Output: Alice

# pop() method removes the specified key and returns the corresponding value. If the key is not found, it raises a KeyError.
print(my_dict.pop('city'))  # Output: New York
print(my_dict)  # Output: {'name': 'Alice', 'country': 'USA'}

# clear() method removes all items from the dictionary.
my_dict.clear()
print(my_dict)  # Output: {}

# copy() method returns a shallow copy of the dictionary.
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
my_dict_copy = my_dict.copy()
print(my_dict_copy)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# update() method updates the dictionary with the key-value pairs from another dictionary or from an iterable of key-value pairs.
my_dict.update({'country': 'USA'})
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}

# fromkeys() method creates a new dictionary with keys from an iterable and values set to a specified value.
keys = ['name', 'age', 'city']
new_dict = dict.fromkeys(keys, 'Unknown')
print(new_dict)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}

# setdefault() method returns the value of a key if it is in the dictionary. If not, it inserts the key with a specified value and returns that value.
print(my_dict.setdefault('name', 'Bob'))  # Output: Alice
print(my_dict.setdefault('country', 'Canada'))  # Output: USA
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'country': 'USA'}

#

