"""
-------------------------------------------------------
List Lab, Task 13
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import union

a = [10, 3, 10, 3, 1]
b = [8, 2, 7, 3, 6, 10, 32, 99]

target = union(a, b)
print("Values 1: {}".format(a))
print("Values 2: {}".format(b))
print()
print("Union: {}".format(target))
