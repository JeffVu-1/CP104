
"""
-------------------------------------------------------
Mortgage payment calculation
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
principal = float(input("Mortgage principal ($): "))
years = int(input("Number of years: "))
rate = float(input("Yearly interest rate (%): "))
months = years * 12
monthly = rate / 100 / 12
top = monthly * (1 + monthly)**months
bottom = (1 + monthly)**months - 1
payment = principal * top / bottom
print()
print("The monthly payments are: $", payment)
