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
from functions import line_numbering

file_handle = open("wilde.txt", "r", encoding="utf-8")
file_handle2 = open("wilde_numbered.txt", "w", encoding="utf-8")
line_numbering(file_handle, file_handle2)
