lst = ['a', 'abc', 'defg', 'hi', 'jkl']

for i in lst:
    if len(i) < 3:
        continue
    else:
        print(i)