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
from functions import extract_date

date = int(input("input a date in the format YYYYMMDD: "))

year, month, day = extract_date(date)

print(f"{year}, {month}, {day}")

