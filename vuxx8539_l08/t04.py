"""
-------------------------------------------------------
List Lab, Task 4
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import generate_integer_list

n = int(input("Number of values: "))
low = int(input("Low value: "))
high = int(input("High value: "))

values = generate_integer_list(n, low, high)
print()
print("Values: {}".format(values))
