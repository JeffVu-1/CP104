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
from functions import interest_table

principal_amount = float(input("Enter a the Principal Amount: "))
interest_rate = float(input("Enter the interest rate: "))
payment = float(input("Enter Payment: "))

interest_table(principal_amount, interest_rate, payment)
