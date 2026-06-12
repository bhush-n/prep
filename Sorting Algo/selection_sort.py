"""
step 1: Search the list and find out the min/max val (We can use the min()/max() built in method)
step 2: Swap the min/max value to 1st index
step 3: Take the sublist(ignore sorted part) and repeat step 1 and 2 untill all the elements are sorted
"""


def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return arr


arr = [56,3,2,78,6,6,0]
select = selectionSort(arr)
print(select)