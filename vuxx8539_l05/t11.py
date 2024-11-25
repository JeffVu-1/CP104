"""
-------------------------------------------------------
Lab 3, Task 11
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import quadrant

for v in [(5, 5), (5, -5), (-5, 5), (-5, -5), (0, 5), (5, 0), (0, 0)]:
    x, y = v
    r = quadrant(x, y)
    print("x: {}, y: {}".format(x, y))
    print("Where: {}".format(r))
    print()
