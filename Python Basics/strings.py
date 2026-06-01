# User input
a = input("Name: ")
print("Hello " + a)

# String Methods
name = "John Doe"
print(name.upper())  # JOHN DOE
print("==================")
print(name.lower())  # john doe
print("==================")
print(name.capitalize())  # John doe
print("==================")
print(name.title())  # John Doe
print("==================")
print(name.strip())  # John Doe
print("==================")
print(name.replace("John", "Jane"))  # Jane Doe
print("==================")
print(name.split())  # ['John', 'Doe']
print("==================")
print(name.split()[0])  # John
print("==================")
print(name.split()[1])  # Doe
print("==================")
print(name.find("Doe"))  # 5   
print("==================")
print(name.startswith("John"))  # True
print("==================")
print(name.endswith("Doe"))  # True
print("==================")
print(name.isalpha())  # False
print("==================")
print(name.isdigit())  # False
print("==================")
print(name.isalnum())  # False
print("==================")
print(name.count("o"))  # 2
print("==================")
print(name.index("o"))  # 1
print("==================")
print(name.rindex("o"))  # 7
print("==================")
print(name.center(20))  # '     John Doe      '