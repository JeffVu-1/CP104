"""
-------------------------------------------------------
String Lab, Task 10
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import text_analyze

s = input("Enter a string: ")
print()
u, l, d, w = text_analyze(s)

print("upper case letters: {}".format(u))
print("lower case letters: {}".format(l))
print("digits: {}".format(d))
print("whitespace characters: {}".format(w))
