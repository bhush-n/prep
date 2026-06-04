def binarySearch(arr, target):
    n = len(arr)
    low = 0
    high = n-1

    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            ans = mid
            low = mid+1
        elif arr[mid] < target:
            low = mid +1
        else:
            high = mid -1
    return ans


arr = [10,20,30,30,30,40,50]
target = 30

bs = binarySearch(arr, target)
print(bs)