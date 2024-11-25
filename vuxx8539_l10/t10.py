"""
-------------------------------------------------------
Lab 9, Task 10
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import count_frequency_word

file = "words.txt"
fv = open(file, "r+")
print("file '{}' open for reading".format(file))
v = input("Word to count: ")
c = count_frequency_word(fv, v)
fv.close()
print("'{}' appears {} time(s)".format(v, c))
