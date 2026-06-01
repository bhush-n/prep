# datatyppes in python
# 1. int ---> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# 2. float  ---> 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5
# 3. str  ---> "Hello", 'World', "Python", 'Programming', "Language", 'Data', "Science", 'Machine', "Learning", 'AI'
# 4. bool ---> True, False
# 5. list ---> [1, 2, 3, 4, 5], ["Hello", "World"], [1, "Python", 3.5], [], [True, False], ["Data", "Science", "Machine", "Learning"], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 6. tuple ---> (1, 2, 3, 4, 5), ("Hello", "World"), (1, "Python", 3.5), (), (True, False), ("Data", "Science", "Machine", "Learning"), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# 7. set ---> {1, 2, 3, 4, 5}, {"Hello", "World"}, {1, "Python", 3.5}, set(), {True, False}, {"Data", "Science", "Machine", "Learning"}, {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# 8. dict ---> {"name": "John", "age": 30, "city": "New York"}, {"name": "Alice", "age": 25, "city": "Los Angeles"}, {"name": "Bob", "age": 35, "city": "Chicago"}, {}, {"name": "Charlie", "age": 40, "city": "Houston"}, {"name": "David", "age": 28, "city": "Phoenix"}, {"name": "Eve", "age": 32, "city": "Philadelphia"}, {"name": "Frank", "age": 27, "city": "San Antonio"}, {"name": "Grace", "age": 29, "city": "San Diego"}, {"name": "Hank", "age": 31, "city": "Dallas"}


print(type(1))  # <class 'int'>
print(type(1.5))  # <class 'float'>
print(type("Hello"))  # <class 'str'>
print(type(True))  # <class 'bool'>
print(type([1, 2, 3, 4, 5]))  # <class 'list'>
print(type((1, 2, 3, 4, 5)))  # <class 'tuple'>
print(type({1, 2, 3, 4, 5}))  # <class 'set'>
print(type({"name": "John", "age": 30, "city": "New York"}))  # <class 'dict'>


# variables in python
name = "John"
age = 30
city = "New York"
print(name)  # John
print(age)  # 30
print(city)  # New York

# naming conventions for variables in python 
# 1. variable names must start with a letter or an underscore
# 2. variable names can only contain letters, numbers, and underscores
# 3. variable names cannot be a reserved keyword in python
# 4. variable names should be descriptive and meaningful

# examples of valid variable names
first_name = "John"
last_name = "Doe"
age = 30
is_student = True

# examples of invalid variable names
# 1name = "John"  # invalid because it starts with a number
# last-name = "Doe"  # invalid because it contains a hyphen
# age! = 30  # invalid because it contains an exclamation mark
# is student = True  # invalid because it contains a space
