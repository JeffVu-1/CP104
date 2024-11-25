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
from functions import pollution_ranking

air_quality_index = int(input("Air quality index: "))
air_type = pollution_ranking(air_quality_index)
print(air_type)