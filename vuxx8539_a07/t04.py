"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "2023-11-16"
-------------------------------------------------------
"""
from functions import list_subtract

minuend = []
subtrahend = []


while True:
    user_input = int(input("Enter a number: "))
    if user_input == 0:
        while True:
            user_input2 = int(input("Enter a target number: "))
            if user_input2 == 0:
                print(minuend)
                print(subtrahend)
                list_subtract(minuend, subtrahend)
                print(minuend)
                break
            else:
                subtrahend.append(user_input2)

        break
    elif user_input >= 0:
        minuend.append(user_input)
    else:
        pass
