"""
-------------------------------------------------------
String Lab, Task 3
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import parse_code

product = input("Enter a product code: ")
c, i, q = parse_code(product)
print("Category:  {}".format(c))
print("ID:        {}".format(i))
print("Qualifier: {}".format(q))
