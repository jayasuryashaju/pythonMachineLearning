"""
this module contains functions for counting vowels in a string and
reversing a string.

for counting vowels count_vowels(string)
for reversing a string rev_str(string)

"""

vowels = 'aeiouAEIOU'


def count_vowels(string):
    count = 0
    for i in string:
        if i in vowels:
            count += 1

    return count


def rev_str(sting):
    return sting[::-1]
