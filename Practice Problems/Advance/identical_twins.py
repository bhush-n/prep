"""
For an array of integers nums, an identical twin is defined as pair (i, j) where nums[i] is equal to nums[j] and i < j.

Examples
Array: [1, 2, 3, 2, 1]
Number of Identical Twins: 2
Explanation:
Identical Twins: [[1, 1], [2, 2]]
Indexes: (0, 4), (1, 3)
"""

def identical_twins(arr):
    n = len(arr)
    res = []    

    for i in range(n):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                res.append([arr[i],arr[j]])
    return res


arr = [1, 2, 3, 2, 1]
it = identical_twins(arr)
print(it)