arr = [1, 0, 2, 0, 3]
res = []

for i in arr:
    if i != 0:
        res.append(i)

while len(res) < len(arr):
    res.append(0)

print(res)
