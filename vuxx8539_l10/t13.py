"""
-------------------------------------------------------
Lab 9, Task 13
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import file_copy

infile = "words.txt"
fv1 = open(infile, "r")
outfile = "new_words.txt"
fv2 = open(outfile, "w")
print("Copying '{}' to '{}'".format(infile, outfile))
file_copy(fv1, fv2)
fv1.close()
fv2.close()
