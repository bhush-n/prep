"""
You have a cube with each edge measuring length a. Find out the surface area and the volume of the cube.

A cube has 6 sides and the formulae for the area and volume are:

Surface Area = 6a2
Volume = a3

Input Format
One line with an integer denoting the side-length of the cube.

Output Format
2 space-separated integers denoting the surface area and volume of the cube respectively.

Examples:

Sample Input
7
Expected Output
294 343

"""

a = int(input("Enter the Number: "))

surface = 6 * a * a
volume = a**3

print(surface, volume)
