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

P = float(input("Principal: $"))
r = float(input("Interest (%): "))
t = int(input("Number of years: "))
n = int(input("Number of times interest compounded per year: "))

A = P * (1 + (r / (100 * n))) ** (n * t)

print("Balance: $ " + str(A))
