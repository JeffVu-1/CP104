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
from functions import student_stats

file_handle = open("students.txt", "r", encoding="utf-8")
l_id, h_id, avg = student_stats(file_handle)
print(l_id, h_id, avg)
