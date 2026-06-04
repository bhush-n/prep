arr = [10,20,30,40,50]

n = len(arr)
left = 0
right = n-1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]

    left += 1
    right -= 1

print(arr)