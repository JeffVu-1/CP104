"""
-------------------------------------------------------
Lab 3, Task 5
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import is_leap

for v in [1900, 1999, 2000, 2004, 1997]:
    r = is_leap(v)
    print("Year: {}".format(v))
    print("Is a leap year: {}".format(r))
    print()
