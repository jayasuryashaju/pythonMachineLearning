"""
lst =  [3, 7, 11, 20, 25, 43, 19, 15, 2, 17]
prime add new list

2.
 lst = ['maths', google, 'ipl', 'jkl', 'mqp', 'swc']
 words with vowel to new lst.
"""

lst = [3, 7, 11, 20, 25, 43, 19, 15, 2, 17]
new_lst = []
for i in lst:
    flag = 0
    for j in range(2, i):
        if i % j == 0:
            flag = 1

    if flag == 0:
        new_lst.append(i)
print(new_lst)


lst = ['maths', 'google', 'ipl', 'jkl', 'mqp', 'swc']

vowels = 'aeiouAEIOU'
new_lst = []

for i in lst:
    for j in i:
        if j in vowels:
            new_lst.append(i)
            break

print(new_lst)

