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
from functions import multiply_fractions

num1 = int(input("input the first numerator: "))
den1 = int(input("input the first denominator: "))
num2 = int(input("input the second numerator: "))
den2 = int(input("input the second denominator: "))

numerator_total, denominator_total, fraction_value = multiply_fractions(num1, den1, num2, den2)

print(f"{numerator_total}, {denominator_total}, {fraction_value} ")