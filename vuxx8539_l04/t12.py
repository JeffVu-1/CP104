"""
-------------------------------------------------------
Lab 4, Task 12
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import c_to_f

celsius = int(input("Enter a temperature (c): "))

fahrenheit = c_to_f(celsius)

print()
print("{:d} C = {:} F".format(celsius, fahrenheit))
