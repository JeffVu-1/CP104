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
from random import randint

HIGH = 100

TAX_RATE = 0.03625
OVERTIME_HOURS = 40
OVERTIME_RATE = 1.5

def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    number = randint(1, high)
    count = 1
    guess = int(input("Please guess a number between 1 and {0}: "
                      .format(high)))

    while guess != number:
        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        count += 1
        guess = int(input("Please guess a number between 1 and {0}: "
                          .format(high)))

    print("Congratulations, you guessed the right number!")
    return count


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 to a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    power = 2

    while power < target:
        power = power * 2
    return power


def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int >= 0)
        current - current population (int > 0)
        rate - percent rate of growth (float)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """
    final = current
    years = 0
    change = 1 + rate / 100

    while final < target:
        years += 1
        final = final * change
    return years


def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """
    num = 1
    final = num * num

    while final < target:
        num += 1
        final += num * num
    return final


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    value = float(input("First positive value: "))
    minimum = value
    maximum = value
    total = value
    count = 1
    value = float(input("Next positive value: "))

    while value >= 0:
        count += 1
        total = total + value

        if value < minimum:
            minimum = value
        elif value > maximum:
            maximum = value
        value = float(input("Next positive value: "))

    average = total / count
    return minimum, maximum, total, average


def num_categories():
    """
    -------------------------------------------------------
    Asks a user to enter a series of numbers, then counts and returns
    how may positives, negatives, and zeroes there are.
    Stop processing values when the user enters -999.
    Use: negatives, zeroes, positives = num_categories()
    -------------------------------------------------------
    Returns:
        negatives - number of negative values (int)
        zeroes - number of zero values (int)
        positives - number of positive values (int)
    ------------------------------------------------------
    """
    negatives = 0
    positives = 0
    zeroes = 0
    value = float(input("First value: "))

    while value != -999:

        if value < 0:
            negatives += 1
        elif value > 0:
            positives += 1
        else:
            zeroes += 1
        value = float(input("Next value: "))

    return negatives, zeroes, positives


def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """

    b_total = 0
    l_total = 0
    s_total = 0
    a_total = 0

    day = 1
    again = 'Y'

    while again == 'Y':
        print("For Day {}:".format(day))
        breakfast = float(input("How much was breakfast? $"))
        lunch = float(input("How much was lunch? $"))
        supper = float(input("How much was supper? $"))
        total = breakfast + lunch + supper
        print("Your total for the day was ${:.2f}".format(total))
        b_total += breakfast
        l_total += lunch
        s_total += supper
        a_total += total
        print()
        again = input("Were you away another day (Y/N)? ").strip()
    return b_total, l_total, s_total, a_total


def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    value = int(
        input("Enter a value between {} and high {}: ".format(low, high)))

    while value < low or value > high:
        if value < low:
            print("Value entered is too low")
        elif value > high:
            print("Value entered is too high")
        value = int(
            input("Enter a value between {} and high {}: ".format(low, high)))
    return value


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced"
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    expenses = 0
    expense = float(input("Enter an expense (0 to quit): $"))

    while expense > 0:
        expenses += expense
        expense = float(input("Enter another expense (0 to quit): $"))

    balance = available - expenses

    if balance < 0:
        status = "Deficit"
    elif balance > 0:
        status = "Surplus"
    else:
        status = "Balanced"
    return expenses, balance, status


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total employee wages (float)
        average - average employee wages (float)
    ------------------------------------------------------
    """
    total = 0
    count = 0
    emp_id = int(input("Employee ID: "))

    while emp_id != 0:
        count += 1
        hourly_rate = float(input("Hourly wage rate: "))
        hours_worked = float(input("Hours worked: "))

        if hours_worked > OVERTIME_HOURS:
            gross_salary = (hours_worked - OVERTIME_HOURS) * \
                hourly_rate * OVERTIME_RATE + OVERTIME_HOURS * hourly_rate
        else:
            gross_salary = hours_worked * hourly_rate

        net_payment = gross_salary - gross_salary * TAX_RATE

        print("Net payment for employee {}: ${:,.2f}".format(emp_id, net_payment))
        total += net_payment
        print()
        emp_id = int(input("Employee ID: "))
    average = total / count
    return total, average
