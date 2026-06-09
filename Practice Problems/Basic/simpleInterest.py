"""Your father has given you some money and you are trying to decide what you want to do with that money. Your friend gives you the idea of an investment that gives you simple interest for your money.

If you invest a sum of p for t years at a rate of r%, the formula for simple interest will be -

Interest = (p*r*t)/100

Given the rate of interest and the time you can invest for, calculate the interest you will recieve.

Input Format
A single line with 3 space-separated parameters: Principal, Rate, Time

Output Format
Interest

The value should be accurate upto exactly 6 decimal places.

Examples:

Sample Input 1
1500 1.4 3
Expected Output
63.000000
"""

principal, rate, time = map(float, input("Enter the value: ").split())

interest = (principal * rate * time) / 100

print(interest)
