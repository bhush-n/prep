"""
Your mother has sent you to the milkman with a cylindrical bottle. You have to pay the milkman the price for the bottle
full of milk at a rate of ₹40 per litre of milk. You are given the radius (r) and the height (h) of the bottle in centimetres.
You can assume the value of π as 3.14.

Formula for volume of cylinder:

V=π r2h

Also, 1 litre = 1000 cm3.

Input Format
1 line containing two space separated integers - the radius and the height of the bottle (in centimetres).

Output Format
The amount you need to pay to the milkman in rupees, accurate upto exactly 2 decimal places.

Examples:

Sample Input
5 24
Expected Output
75.36
"""

r, h = map(float, input("Enter the values: ").split())
pie = 3.14

v = pie * ((r**2) * h)
litres = v / 1000

amount = litres * 40

print(amount)
