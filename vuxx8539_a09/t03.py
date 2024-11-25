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

from functions import file_statistics

file_handle = open("addresses.txt", "r", encoding="utf-8")
ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
print(ucount, lcount, dcount, wcount, rcount)
