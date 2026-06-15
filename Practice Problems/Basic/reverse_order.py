def reverse_order(n):
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = (reversed_n * 10) + digit
        n = n // 10
    return reversed_n

n = 2334
ro = reverse_order(n)
print(ro)