"""
-------------------------------------------------------
Lab 6, Task 14
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import ia_hours

WEEKS = 6

ia_count = int(input("Number of IAs: "))
total_hours = ia_hours(ia_count)
print()
print("Total hours: {:.2f}".format(total_hours))
