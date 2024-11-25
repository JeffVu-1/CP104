"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import range_addition

start = int(input("Enter the start value: "))
increment = int(input("Enter the increment value: "))
count = int(input("Enter the count value: "))
total = range_addition(start, increment, count)
print(total)
