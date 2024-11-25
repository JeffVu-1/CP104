"""
-------------------------------------------------------
Lab 11, Task 13
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import generate_matrix_num, print_matrix_num, scalar_multiply

matrix = generate_matrix_num(4, 3, -10, 10, "int")
print("Matrix before scalar multiplication:")
print_matrix_num(matrix, "int")
n = 5
print("n: {}".format(n))
scalar_multiply(matrix, n)
print("Matrix after scalar multiplication:")
print_matrix_num(matrix, "int")
