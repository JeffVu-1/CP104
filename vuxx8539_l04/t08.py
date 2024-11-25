"""
-------------------------------------------------------
Lab 4, Task 8
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import computer_costs

computer_cost = float(input("Cost of each computer: "))
computers_bought = int(input("Number of computers bought: "))
commission_percent = float(input("Wholesaler commission: "))

pre_commission_cost, total_cost = computer_costs(
    computer_cost, computers_bought, commission_percent)

print()
print("Cost of computers (no commission): ${:10,.2f}".format(
    pre_commission_cost))
print("Cost of computers (total):         ${:10,.2f}".format(total_cost))
