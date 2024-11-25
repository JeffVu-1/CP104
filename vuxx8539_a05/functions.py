"""
-----------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
---------------------------------------------------
"""

def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """

    product = 1
    for i in range(1, number+1):
        product = product * i

    return product


def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Calculates the amount of calories burned at each interval of five minutes
    Use: calories_treadmill(per_minute, minutes)
    -------------------------------------------------------
    Parameters:
        per_minute - the number of calories burned per minute (float >= 0)
        minutes - the total number of minutes on the treadmill (int >= 0)
    Returns: None
    ------------------------------------------------------
    """

    for i in range(5, minutes+1, 5):
        calories_burned_per_five_minutes = per_min * i
        print(f" {i:2d} {calories_burned_per_five_minutes:.1f}")
    return


def arrow_up(rows):
    """
    -------------------------------------------------------
    Prints a arrow with the specified number of rows using the # symbol
    Use: arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - the number of rows to be printed (int > 0)
    Returns: None
    ------------------------------------------------------
    """
    for i in range(1, rows+1):
        if i == 1:
            print(" " * (rows - i) + "#")
        else:
            print(" " * (rows - i) + "#" + " " * (2 * i - 3) + "#")
    return


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """

    number = (stop_num - start_num) + 1
    lines = "-----"

    for i in range(start_num, stop_num + 1):

        if i == start_num:
            print(f"       {i:>5}", end="")

        else:
            print(f"{i:>5}", end="")

    print()

    print(f"       {lines * number}")

    for i in range(start_num, stop_num + 1):

        print(f"{i:>5} |", end="")

        for j in range(start_num, stop_num+1):

            print(f"{i * j:>5}", end="")

        print()

    return


def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """

    number = 0

    for i in range(0, count):
        number += start + i * increment

    return number
