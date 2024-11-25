"""
-------------------------------------------------------
Lab 11, Task 6
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import generate_matrix_num, print_matrix_num, stats

matrix = generate_matrix_num(3, 4, -10, 10, "int")
print_matrix_num(matrix, 'int')
smallest, largest, total, average = stats(matrix)
print()
print("Smallest = {}".format(smallest))
print("Largest = {}".format(largest))
print("Total = {}".format(total))
print("Average = {:.2f}".format(average))
