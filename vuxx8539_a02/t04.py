"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""

num_flyer = int(input("Number of flyers: "))
num_delivery = int(input("Number of delivery people: "))

flyer_PerPerson = num_flyer // num_delivery

left_overFlyers = num_flyer % num_delivery

print(f"Flyers per delivery person: {flyer_PerPerson}")
print(f"Flyers left over: {left_overFlyers}")
