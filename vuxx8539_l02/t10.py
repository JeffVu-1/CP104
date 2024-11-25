"""
-------------------------------------------------------
Calculate total amount of meal including inputted tip and sales tax
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""

food = float(input("Food Charge: $"))
tax_percent = float(input("Sales Tax in (%): "))
tip_percent = float(input("Tip in (%): "))

tax_decimal = tax_percent / 100
tip_decimal = tip_percent / 100

tax = food * tax_decimal
tip = food * tip_decimal
total = tax + tip + food

print()
print("Subtotal: $", food)
print("     Tax: $", tax)
print("     Tip: $", tip)
print("------------------")
print("   Total: $", total)
