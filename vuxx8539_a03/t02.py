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
from functions import lawn_mow_time

Width_of_lawn = float(input("Width of lawn (meters): "))
Length_of_lawn = float(input("Height of lawn (meters): "))
cutting_speed = float(input("Speed of lawn: "))

total_time = lawn_mow_time(Width_of_lawn, Length_of_lawn, cutting_speed)

print(total_time)
