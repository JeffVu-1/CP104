"""
-------------------------------------------------------
Lab 9, Task 7
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import append_max_num

file = "numbers.txt"
fv = open(file, "r+")
print("file '{}' open for reading and writing".format(file))
num = append_max_num(fv)
fv.close()
print("{} is appended".format(num))
