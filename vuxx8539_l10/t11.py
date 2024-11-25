"""
-------------------------------------------------------
Lab 9, Task 11
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import find_longest

file = "words.txt"
fv = open(file, "r+")
print("file '{}' open for reading".format(file))
w = find_longest(fv)
fv.close()
print("'{}' is the last longest word".format(w))
