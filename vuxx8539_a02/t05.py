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

Found_Length = float(input("Foundation length (m): "))
Found_Width = float(input("Foundation width (m): "))
Found_Hieght = float(input("Foundation height (m): "))
w_height = float(input("Wall height (m): "))
Cost_ofCon_Meters3 = float(input("Cost of concrete ($/m^3): "))
Cost_ofBrick_Meters2 = float(input("Cost of bricks ($/m^2): "))

Concrete_needed_for_foundation = (Found_Length * Found_Width * Found_Hieght)
Cost_of_concrete = Concrete_needed_for_foundation * Cost_ofCon_Meters3
Bricks_needed_for_walls = (
    (Found_Length * w_height) + (Found_Width * w_height))*(2)
Cost_ofBricks = Cost_ofBrick_Meters2 * Bricks_needed_for_walls
total_cost = Cost_ofBricks + Cost_of_concrete


print(
    f"\nConcrete needed for foundation (m^3): {Concrete_needed_for_foundation:,.2f}")
print(f"Cost of concrete: ${Cost_of_concrete:,.2f}")
print(f"Bricks needed for walls (m^2): {Bricks_needed_for_walls:,.2f}")
print(f"Cost of bricks: ${Cost_ofBricks:,.2f}")
print(f"Total cost: ${total_cost:,.2f}")
