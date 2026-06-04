arr = [10, 80, 50, 70]
largest = arr[0]
second = float('-inf')

for i in arr:
    if i > largest:
        second = largest
        largest = i
    elif i > second:
        second = i
    
print(second)