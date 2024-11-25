"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from functions import get_indexes

pos_list = []
while True:
    user_input = int(input("Enter a number: "))
    if user_input == 0:
        target_number = int(input("Enter a target number: "))
        break
    elif user_input >= 0:
        pos_list.append(user_input)
    else:
        pass

answer = get_indexes(pos_list, target_number)
print(answer)
