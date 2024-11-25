"""
-------------------------------------------------------
Lab 5, Task 2
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import get_weight

for v in [0.1, 0.5, 4, 5, 150, 300]:
    n, m = get_weight(v)
    print("Mass: {}".format(v))
    print("Newtons: {}, Message: {}".format(n, m))
    print()
