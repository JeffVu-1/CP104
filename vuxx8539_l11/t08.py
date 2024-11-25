"""
-------------------------------------------------------
Lab 11, Task 8
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import generate_matrix_num, print_matrix_num, find_less

matrix = generate_matrix_num(4, 3, -10, 10, "int")
print_matrix_num(matrix, 'int')
s = find_less(matrix, 6)
print()
print("Position: {} ".format(s))
print("Value: {}".format(matrix[s[0]][s[1]]))
