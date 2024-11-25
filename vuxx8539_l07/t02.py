"""
-------------------------------------------------------
Lab: Repetition - While
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import power_of_two

targets = [2, 3, 8, 9, 255, 256, 257]

for target in targets:
    p = power_of_two(target)
    print("The closest power of 2 >= {0} is {1}".format(target, p))
    print()
