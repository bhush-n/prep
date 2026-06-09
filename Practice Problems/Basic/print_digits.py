"""
Given a two-digit number n, print both the digits of the number.

Input Format
The first line indicating the number of test cases T.

Next T lines will each contain a single number ni.

Output Format
T lines each containing two digits of the number ni separated by space.

Examples
Sample Input
2
34
45
Expected Output
3 4
4 5

"""

t = int(input("Enter the number: "))

for i in range(t):
    n = input("Enter the iterative number: ")
    print(n[0], n[1])
