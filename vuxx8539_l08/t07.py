"""
-------------------------------------------------------
List Lab, Task 7
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import generate_integer_list, list_categorize

n = int(input("Number of values: "))
low = int(input("Low value: "))
high = int(input("High value: "))

values = generate_integer_list(n, low, high)
print()
print("Values: {}".format(values))
n, p, z, e, o = list_categorize(values)
print()
print("Negatives: {}".format(n))
print("Positives: {}".format(p))
print("Zeroes: {}".format(z))
print("Evens: {}".format(e))
print("Odds: {}".format(o))
