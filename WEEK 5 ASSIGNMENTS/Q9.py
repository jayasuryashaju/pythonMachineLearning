product = 0
for i in range(1, 10):
    for j in range(1, 10):
        product = i * j
        if product <= 10:
            continue
        else:
            break
    if product > 10:
        print(i, j)
        break
