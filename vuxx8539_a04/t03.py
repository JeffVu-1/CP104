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
from functions import largest_average

val1 = float(input("Value 1: "))
val2 = float(input("Value 2: "))
val3 = float(input("Value 3: "))

largest_average = largest_average(val1, val2, val3)
print(largest_average)