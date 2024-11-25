"""
-------------------------------------------------------
List Lab, Task 9
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import many_search


a = [94, 96, -22, -79, -28, 96, -50, 71, 24, -32]
print(a)
print()

for v in a:
    i = many_search(a, v)
    print("Index of {}: {}".format(v, i))

v = 999
i = many_search(a, v)
print("Index of {}: {}".format(v, i))
