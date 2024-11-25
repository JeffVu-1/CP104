"""
-------------------------------------------------------
Lab 3, Task 9
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import wind_speed

for v in [-1, 1, 39, 62, 89, 118]:
    r = wind_speed(v)
    print("Speed: {}".format(v))
    print("Category: {}".format(r))
    print()
