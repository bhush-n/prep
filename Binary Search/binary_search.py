"""
INPUT: ALways a sorted list


step 1: Start search with sorted List
step 2: set 2 pointers 
    1] low: one at the beginning
    2] high: one at the last index
step 3: When low is less than or equal to high
    1] Find the middle element between low and high
    2] Check if the middle element is our target if yes: return index
    If not :
        a]Check middle element is less than target if yes: move low to one position after middle element and repeat step 3
        b]Check the middle element is greater than target if yes: move high to one position before middle element and repeat s3
step 4: If low pointer goes beyond high pointer target is not present in the list: return -1
"""
def binarySearch(arr, target):
    n = len(arr)
    low = 0
    high = n-1

    while low <= high:
        mid = (low+high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid -1
    return -1

arr = [10,20,30,40,50]
target = 50 

bs = binarySearch(arr,target)
print(bs)
