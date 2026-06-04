"""
step 1: Starting with the 1st index (arr[0]) compare the current element with next index element of array
step 2: If the current element is greater that next element: SWAP them 
step 3: If the current element is less than next element: MOVE to next element and repeat STEP 1    
"""

def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr


arr = [56,3,2,78,6,6,0]
bubble = bubbleSort(arr)
print(bubble)