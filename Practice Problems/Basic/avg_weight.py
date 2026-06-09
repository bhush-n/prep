"""
Your teacher has assigned you the task of finding out the average weight of your class.
She gives you the weights of all the students in the class and expects you to calculate the average weight of the class.
Assume that there are only 10 students in your class.

Input Format
A single line with 10 space separated weights

w1 w2 w3 w4 w5 w6 w7 w8 w9 w10

Output Format
A single value - The average weight

The value should be accurate upto exactly 6 decimal places.

Examples:

Sample Input
40.75 45.2 55.3 49.5 43.3 54.1 38.4 63.8 45.2 58.25
Expected Output
49.380000
"""

n = float(input())
arr = list(map(float, input().split()))

avg = sum(arr) // len(arr)

print(avg)
