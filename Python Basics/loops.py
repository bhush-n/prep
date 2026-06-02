# For loop

# for i in range(5):
#     print(i)

# range() function generates a sequence of numbers from 0 to n-1 where n is the argument passed to the function. 
# range(start, stop, step) generates a sequence of numbers from start to stop-1 with a step of step.

for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# enumerate() function adds a counter to an iterable and returns it as an enumerate object.
# enumerate(iterable, start=0) returns an enumerate object that contains pairs of index and value from the iterable.

fruits = ['apple', 'banana', 'orange']
for index, value in enumerate(fruits):
    print(index, value)  # 0 apple, 1 banana, 2 orange

# while loop
i = 0
while i < 10:
    print(i)  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    i += 1

# break statement
i = 0
while True:
    print(i)  # 0, 1, 2, 3, 4
    i += 1
    if i == 5:
        break
    
