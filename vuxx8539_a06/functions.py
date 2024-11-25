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

def total_wins():
    """
    -------------------------------------------------------
    Returns the number of times each input appears
    Use: purple, gold = total_wins()
    -------------------------------------------------------
    Parameters: None
    Returns: 
        purple - number of occurrences of 'purple' in list (int)
        gold - number of occurrences of 'gold' in list (int)
    -------------------------------------------------------
    """
    teams = []
    team = str(input("Enter winning team: "))

    while team != "":
        teams.append(team)
        team = str(input("Enter winning team: "))

    purple = teams.count("purple")
    gold = teams.count("gold")

    return purple, gold


def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """

    var = None
    if number == 1:
        var = False
    elif number == 2:
        var = True
    else:
        i = 2
        while i < number:
            if number % i == 0:
                var = False
            i += 1
        var = True
        return var


def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    MONTHLY_INTEREST = ((interest_rate/12) / 100)
    MONTH = 1

    print(f"Principal: ${principal_amount:.2f}")
    print(f"Interest Rate: {interest_rate:.2f}%")
    print(f"Monthly Payment: {payment:.2f}")
    print("----------------------------------")
    print("Month Interest   Payment   Balance")
    print("----------------------------------")

    while principal_amount > 0:
        interest_amount_for_each_month = (principal_amount * MONTHLY_INTEREST)
        remaining_balance = interest_amount_for_each_month + principal_amount - payment
        principal_amount = remaining_balance
        if remaining_balance < payment:

            print(
                f"{MONTH:5}{interest_amount_for_each_month:9.2}{payment:10.2f}{remaining_balance:10.2f}")
            payment = remaining_balance
            remaining_balance = 0
            MONTH += 1
            interest_amount_for_each_month = (
                principal_amount * MONTHLY_INTEREST)
            print(
                f"{MONTH:5}{interest_amount_for_each_month:9.2f}{payment:10.2f}{remaining_balance:10.2f}")
            break
        else:
            print(
                f"{MONTH:5}{interest_amount_for_each_month:9.2f}{payment:10.2f}{remaining_balance:10.2f}")
            MONTH += 1
    return


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    number = abs(number)
    amount_of_digits = 0

    while number != 0:
        number //= 10
        amount_of_digits += 1

    return amount_of_digits


def factor_summation(number):
    """
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    """
    total = 0
    i = 1

    while i < number:
        if number % i == 0:
            total += i
        i += 1

    return total
