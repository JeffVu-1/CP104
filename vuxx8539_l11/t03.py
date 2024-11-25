"""
-------------------------------------------------------
Lab 11, Task 3
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import generate_matrix_num, print_matrix_num

matrix = generate_matrix_num(3, 4, -10, 10, "float")
print_matrix_num(matrix, 'float')
print("---------------------------------------")
matrix = generate_matrix_num(4, 3, -10, 10, "float")
print_matrix_num(matrix, 'float')

cols = 3
stuff = list(range(cols))
print(stuff)
rows = 4
string = ".*" + \
    "".join([str(i) + "\D*" + str(matrix[i][0]) + ".*" for i in range(rows)])
print(string)

string = ".*" + "\D*".join(
    ["{:.2f}".format(matrix[-1][i]) for i in range(cols)]) + "$"
print(string)


# ^\D*0\D5.*1\D*7.*2\D*9.*
