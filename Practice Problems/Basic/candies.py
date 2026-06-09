"""
You are having a get together at your house and your mother asks you to distribute candies equally amongst all your cousins.
You want to determine if the number of candies given by your mother can be equally distributed or not.

Input Format
A single line with two space-separated integers representing the number of candies and the number of cousins repectively.

Output Format
Print "YES" if you can equally distribute the candies and "NO" if you cannot.

Examples:

Sample Input 1
35 10
Expected Output
NO
Explanation
You can't distribute 25 candies equally among 10 cousins.
"""

candies, cousins = map(int, input("enter the value: ").split())

if cousins % candies == 0:
    print("YES")
else:
    print("NO")
print(candies % cousins)
