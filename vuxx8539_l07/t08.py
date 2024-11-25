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
from functions import budget

available = float(input("Monthly budget: $"))
expenses, balance, status = budget(available)
print()
print("Total Expenses: ${:.2f}".format(expenses))
print("{}: ${:.2f}".format(status, balance))
