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
from functions import employee_payroll

total, average = employee_payroll()
print()
print("Total payment:   ${:8.2f}".format(total))
print("Average payment: ${:8.2f}".format(average))
