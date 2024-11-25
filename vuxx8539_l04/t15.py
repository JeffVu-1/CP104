"""
-------------------------------------------------------
Lab 4, Task 15
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import time_split

initial_seconds = int(input("Number of seconds: "))

days, hours, minutes, seconds = time_split(initial_seconds)

print()
print("Days: {:d}, Hours: {:d}, Minutes: {:d}, Seconds: {:d}".format(
    days, hours, minutes, seconds))
