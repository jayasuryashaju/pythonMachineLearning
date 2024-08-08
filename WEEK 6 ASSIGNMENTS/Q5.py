from fibanocci import *

n = int(input('Enter a number : '))
if n < 0:
    print('invalid input')
else:
    print(f"The {n}th Fibonacci number is: {fibonacci(n)}")