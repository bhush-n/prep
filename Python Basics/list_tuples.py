# Lists

x = [1, 2, 3, 4, 5]
print(x)  # [1, 2, 3, 4, 5]

x = [1, "Hello", 3.5, True]
print(x)  # [1, 'Hello', 3.5, True]

# length of a list
x = [1, 2, 3, 4, 5]
print(len(x))  # 5

# append method
x = [1, 2, 3, 4, 5]
x.append(6)
print(x)  # [1, 2, 3, 4, 5, 6]

# extend method
x = [1, 2, 3, 4, 5]
x.extend([6, 7, 8])
print(x)  # [1, 2, 3, 4, 5, 6, 7, 8]

# insert method
x = [1, 2, 3, 4, 5]
x.insert(0, 0)
print(x)  # [0, 1, 2, 3, 4, 5]

# remove method
x = [1, 2, 3, 4, 5]
x.remove(3)
print(x)  # [1, 2, 4, 5]

# pop method
x = [1, 2, 3, 4, 5]
x.pop(2)
print(x)  # [1, 2, 4, 5]

# indexing of a list
x = [1, 2, 3, 4, 5]
print(x[0])  # 1
print(x[1])  # 2

# slicing of a list
x = [1, 2, 3, 4, 5]
print(x[0:3])  # [1, 2, 3]
print(x[2:])  # [3, 4, 5]
print(x[:3])  # [1, 2, 3]
print(x[:])  # [1, 2, 3, 4, 5]

