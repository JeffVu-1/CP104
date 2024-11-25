"""
-------------------------------------------------------
Lab 5, Task 12
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import gic

for values in [(1000, 10, 5), (1000, 25, 2.0)]:
    print("Values: {}".format(values))
    print()
    gic(*values)
    print()
