"""
Given a number, find out if it is odd or even.

There are multiple tests in this.

Input Format
First line indicating the number of test cases T.

Next T lines containing a number each ni where i denotes the ith input.

Output Format
T lines each indicating the answer for the ith input.

Each line says "ODD" if the number is odd and "EVEN" if the number is even.

Examples:

Sample Input
4
23
12
44
32
Expected Output
ODD
EVEN
EVEN
EVEN

"""

t = int(input())

for i in range(t):
    n = int(input())

    if n % 2 == 0:
        print("EVEN")
    else:
        print("ODD")
