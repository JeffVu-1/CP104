"""
-------------------------------------------------------
Lab 4, Task 5
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import right_triangle

adjacent = float(input("Length of adjacent side: "))
opposite = float(input("Length of opposite side: "))

hyp, circ, area = right_triangle(adjacent, opposite)

print()
print("Hypotenuse of triangle: {:.2f}".format(hyp))
print("Circumference of triangle: {:.2f}".format(circ))
print("Area of triangle: {:.2f}".format(area))
