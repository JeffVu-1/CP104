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
from functions import footage_to_acres

amount_feet = float(input("Enter amount of footage: "))

answer = footage_to_acres(amount_feet)

print(answer)