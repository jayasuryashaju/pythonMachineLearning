"""
importing functions to count vowels and reversing a string
from my_functions

"""

from my_functions import count_vowels, rev_str

string = input("enter a string : ")

print(f'the count of vowels in the string = {count_vowels(string)}')

print(f'the reverse of the string = {rev_str(string)}')