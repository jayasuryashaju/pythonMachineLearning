words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
skip_words = ['banana', 'date']

for i in words:
    if i in skip_words:
        continue
    else:
        print(i)