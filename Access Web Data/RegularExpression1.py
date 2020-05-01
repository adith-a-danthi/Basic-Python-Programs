"""
Extract all the numbers in the file and compute the sum of the numbers.
"""

import re

file_name = input("Enter file name: ")
file = open(file_name, 'r')

res = 0
count = 0
for line in file:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        res = res + int(number)

print(res)
