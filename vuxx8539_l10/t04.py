"""
-------------------------------------------------------
Lab 9, Task 4
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import customer_first

print("Find customer with earliest sign-in:")
fv = open("customers.txt", "r")
data = customer_first(fv)
fv.close()
print(data)
