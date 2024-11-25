"""
-------------------------------------------------------
Lab 6, Task 7
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import draw_arrow

for values in [(0, '#'), (1, '#'), (4, '*'), (6, '#')]:
    print("Values: {}".format(values))
    print()
    draw_arrow(*values)
    print()
