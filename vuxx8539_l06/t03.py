"""
-------------------------------------------------------
Lab 6, Task 3
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import sum_all

for nums in [(1, 1, 1), (5, 10, 1), (10, 100, 10)]:
    total = sum_all(*nums)
    print('sum_all({}) = {}'.format(nums, total))
    print()
