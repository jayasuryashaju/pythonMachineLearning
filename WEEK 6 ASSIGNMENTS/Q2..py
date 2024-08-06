"""
importing package named my_package which have functions to add and subtract 2 numbers.
module_1 have function add(num1, num2)
module_2 have function sub(num1, num2)
"""
from my_package.module_1 import add
from my_package.module_2 import sub

num1 = int(input('enter a number : '))
num2 = int(input('enter a number : '))

print(f'the sum of the numbers = {add(num1, num2)}')
print(f'the difference of the two numbers = {sub(num1, num2)}')