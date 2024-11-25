"""
-------------------------------------------------------
String Lab, Task 14
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import str_distance

line1 = input("Enter first string: ")
line2 = input("Enter second string: ")
print()
d = str_distance(line1, line2)
print("Distance: {}".format(d))
