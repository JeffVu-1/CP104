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

TAX_RATE = 18.50
sales = float(input("Enter the total sales: $"))
tax_precentage = TAX_RATE / 100
tax = sales*tax_precentage
print("\nProjected Tax Report")
print("--------------------------")
print(f"Total sales:    $ {sales:,.2f}")
print("Annual tax:     % 18.50")
print("--------------------------")
print(f"Tax:            $ {tax:,.2f}")
