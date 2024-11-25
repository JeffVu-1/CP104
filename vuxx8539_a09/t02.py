"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import read_integers

file_handle = open("numbers.txt", "r")
number_list = read_integers(file_handle)
print(number_list)
