"""
-------------------------------------------------------
String Lab, Task 1
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import is_hydroxide

chemical = input("Enter a chemical formula: ")

hydroxide = is_hydroxide(chemical)

if hydroxide:
    print("{} is a hydroxide.".format(chemical))
else:
    print("{} is not a hydroxide.".format(chemical))
