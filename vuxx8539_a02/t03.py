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

date = int(input("Enter a date in the format YYYYMMDD: "))
year = date // 10000
month = (date // 100) % 100
day = date % 100

formatted_date = f"{year}/{month:02}/{day:02}"
print("\nThe reformatted date:", formatted_date)
