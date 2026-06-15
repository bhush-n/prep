"""
Initial Array: [1, 2, 3, 4]
Cumulative Sum: [1, 3, 6, 10]
"""

def cumulative_sum(arr):
    res = []
    sum = 0
    for i in arr:
        sum += i
        res.append(sum) 
    return res


arr = [1, 2, 3, 4]
cs = cumulative_sum(arr)
print(cs)