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

def list_factors(number):
    """
    -------------------------------------------------------
    Gets a list of all the factors of the given number, excluding the number itself
    Use: factors = list_factors(num)
    -------------------------------------------------------
    Parameters:
        num - the number that needs to be factorized (int > 0)
    Returns:
        factors - a list that contains all the factors of num (list of int)
    ------------------------------------------------------
    """

    index = []
    for i in range(1, number):
        if number % i == 0:
            index.append(i)
    return index


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """

    pos_list = []
    while True:
        user_input = int(input("Enter a number "))
        if user_input == 0:
            return pos_list
        elif user_input >= 0:
            pos_list.append(user_input)
        else:
            pass


def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """
    index_list = []
    for i in range(len(numbers)):
        if numbers[i] == target_number:
            index_list.append(i)
    return index_list


def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """
    remove_num = []
    for i in minuend:
        for j in subtrahend:
            if i == j:
                remove_num.append(i)
    for i in remove_num:
        minuend.remove(i)

    return


def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """

    sorted_numbers = sorted(numbers)

    if numbers == sorted_numbers:
        in_order = True
        index = -1
    else:
        in_order = False
        index = 1

    return in_order, index
