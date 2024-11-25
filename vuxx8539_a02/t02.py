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

pos_num = int(input("Enter a positive digit number: "))
first_digit = pos_num // 10
second_digit = pos_num % 10
difference = first_digit - second_digit
print("\nThe difference of the digits of", pos_num, "is", difference)
