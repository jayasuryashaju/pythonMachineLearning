lst = [1, 4, 2, 5, -1, 3, -4, 4, 2, -7, -5]
result = 0
for i in lst:
    if i < 0:
        continue
    else:
        result += i

print(result)