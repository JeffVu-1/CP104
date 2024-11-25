"""
-------------------------------------------------------
Prints a table of materials
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
dirt = float(input("Enter amount of dirt (m^3): "))
gravel = float(input("Enter amount of gravel (m^3): "))
sand = float(input("Enter amount of sand (m^3): "))
total = dirt + gravel + sand
print()
print("Material   Cubic Metres")
print(f"Dirt       {dirt:5.1f}")
print(f"Gravel     {gravel:5.1f}")
print(f"Sand       {sand:5.1f}")
print(f"Total      {total:5.1f}")
