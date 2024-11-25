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
from functions import calories_treadmill

calories_burned_permin = float(input("give a number of calories burned per minute: "))
minutes = int(input("give a number of minutes: "))
calories_treadmill(calories_burned_permin, minutes)
