"""
Two Sum
Easy
Given an array A and an integer target, find the indices of the two numbers in the array whose sum is equal to the given target.

Note: The problem has exactly one solution. Do not use the same element twice.

Example
A: [1, 3, 3, 4]
target: 5
Answer: [0, 3]
"""

def two_sum(arr,target):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                return [i,j]


arr = [1, 3, 3, 4]
target= 5

ts = two_sum(arr, target)
print(ts)