"""
You and your friend decide to play a game where given some numbers, you have to find the maximum number.
If the maximum is an even number, you win and if it is odd, your friend wins.

Input Format
Two lines:

First line contains a single integer N
Second line contains N space separated integers
N
n1 n2 n3 ..... nN
Output Format
Your winning status. If you win, print WON and if you lose, print LOST.

Examples:

Sample Input
5
12 45 234 5674 122
Expected Output
WON

"""

n = int(input())
arr = list(map(int, input().split()))

maximum = max(arr)

if maximum % 2 == 0:
    print("WON")
else:
    print("LOST")
