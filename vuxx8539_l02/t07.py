"""
-------------------------------------------------------
A charity asks volunteers to distribute flyers for an event. They want
to distribute the flyers evenly amongst the volunteers. Write and test
a program that prompts the user to enter the number of flyers and the
number of volunteers, and prints the number of flyers per volunteer and
the number of flyers left over.The resulting program should look like:

Number of flyers: 10000
Number of volunteers: 22
Flyers per volunteer: 454
Flyers left over: 12

Your program must use the integer division ( // ) and modulus ( % ) operators.

Run this program three times with three different sets of data. Display
the results with the comma as the thousands separator.
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
    
flyers = int(input("Number of flyers: "))
volunteers = int(input("Number of volunteers: "))

flyers_per_person = flyers // volunteers
flyers_left = flyers % volunteers
print()
print("Flyers per volunteer:", flyers_per_person)
print("Flyers left over:", flyers_left)

