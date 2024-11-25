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
TAX_RATE = 0.03625
OVERTIME_HOURS = 40
OVERTIME_RATE = 1.5

DISCOUNT_RATE = 0.05

BASIC_RAISE = 0.02
FULL_LONG = 0.05
FULL_SHORT = 0.015
PART_LONG = 0.03
PART_SHORT = 0.01

GRAVITY_ACCEL = 9.8 

MIN_YEARS = 5
MIN_SALARY = 30000

SENIOR_AGE = 65
SENIOR_PRICE = 4.0
ADULT_AGE = 18
ADULT_PRICE = 5.0
INFANT_AGE = 3
INFANT_PRICE = 0
STUDENT_AGE = 10
STUDENT_PRICE = 3.0
THIS_SCHOOL = 1.0
KID_PRICE = 2.0

BURGER = 6.0
WINGS = 8.0
COMBO_S = 2.0
COMBO_F = 1.5


def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        result - True if day times month equals year, False otherwise (boolean)
    -------------------------------------------------------
    """
    assert day > 0, "day must be > 0"
    assert month > 0, "month must be > 0"
    assert year > 0, "year must be > 0"

    if day * month == year:
        result = True
    else:
        result = False
    return result


def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg) &times; acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        newtons - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    newtons = mass * GRAVITY_ACCEL

    if newtons > 1000:
        message = "heavy"
    elif newtons < 10:
        message = "light"
    else:
        message = "average"
    return newtons, message


def gym_cost(cost, friends):
    """
    -------------------------------------------------------
    Calculates total cost of a gym membership.
    Use: final_cost = gym_cost(cost, friends)
    -------------------------------------------------------
    Parameters:
        cost - a gym membership base cost (float > 0)
        friends - number of friends signed up (int >= 0)
    Returns:
        final_cost - cost of membership after discount (float)
    ------------------------------------------------------
    """
    if friends == 1:
        final_cost = cost * (1 - DISCOUNT_RATE)
    elif friends == 2:
        final_cost = cost * (1 - DISCOUNT_RATE * 2)
    elif friends >= 3:
        final_cost = cost * (1 - DISCOUNT_RATE * 3)
    else:
        final_cost = cost
    return final_cost


def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    d1 = abs(target - v1)
    d2 = abs(target - v2)

    if d1 > d2:
        result = v2
    else:
        result = v1
    return result


def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (bool)
    ------------------------------------------------------
    """
    if year % 400 == 0:
        result = True
    elif year % 100 == 0:
        result = False
    elif year % 4 == 0:
        result = True
    else:
        result = False
    return result


def is_divisible(n, i, j):
    """
    -------------------------------------------------------
    Determines if n is evenly divisible by both i and j.
    Use: result = is_divisible(n, i)
    -------------------------------------------------------
    Parameters:
        n - the number to check for divisibility (int)
        i - one of the values to divide n by (int)
        j - another value to divide n by (int)
    Returns:
        result - True if n is evenly divisible by both
            i and j, False otherwise (bool)
    ------------------------------------------------------
    """
    result = n % i == 0 and n % j == 0
    return result


def get_pay(hourly_rate, hours_worked):
    """
    -------------------------------------------------------
    Calculates an employee's net wage given hours and pay.
    Each employee is paid 1.5 times their regular hourly rate for
    all hours over 40. A tax amount of 3.625 percent of gross salary
    is deducted.
    Use: net_payment = get_pay(hourly_rate, hours_worked)
    -------------------------------------------------------
    Parameters:
        hourly_rate - hourly rate of pay (float)
        hours_worked - total hours worked (float)
    Returns:
        net_payment - description (float)
    ------------------------------------------------------
    """
    if hours_worked > OVERTIME_HOURS:
        gross_salary = (hours_worked - OVERTIME_HOURS) * \
            hourly_rate * OVERTIME_RATE + OVERTIME_HOURS * hourly_rate
    else:
        gross_salary = hours_worked * hourly_rate

    net_payment = gross_salary - gross_salary * TAX_RATE
    return net_payment


def roman_numeral(n):
    """
    -------------------------------------------------------
    Convert 1-10 to Roman numerals.
    Use: numeral = roman_numeral(n)
    -------------------------------------------------------
    Parameters:
        n - number to convert to Roman numerals (int)
    Returns:
        numeral - Roman numeral version of n, None if n is not
          between 1 and 10 inclusive.
    -------------------------------------------------------
    """
    if n == 1:
        numeral = "I"
    elif n == 2:
        numeral = "II"
    elif n == 3:
        numeral = "III"
    elif n == 4:
        numeral = "IV"
    elif n == 5:
        numeral = "V"
    elif n == 6:
        numeral = "VI"
    elif n == 7:
        numeral = "VII"
    elif n == 8:
        numeral = "VIII"
    elif n == 9:
        numeral = "IX"
    elif n == 10:
        numeral = "X"
    else:
        numeral = None
    return numeral


def wind_speed(speed):
    """
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """
    if speed < 0:
        category = "Unknown"
    elif speed < 39:
        category = "Breeze"
    elif speed < 62:
        category = "Strong Wind"
    elif speed < 89:
        category = "Gale Winds"
    elif speed < 118:
        category = "Whole Gale"
    else:
        category = "Hurricane"
    return category


def richter(intensity):
    """
    -------------------------------------------------------
    Determines damage level given earthquake intensity measured
    on the Richter scale.
    Use: result = richter(intensity)
    -------------------------------------------------------
    Parameters:
        intensity - Richter scale number for severity of earthquake
            (float >= 0)
    Returns:
        result - astring describing earthquake damage (str)
    -------------------------------------------------------
    """
    assert intensity >= 0, "intensity must be >= 0"

    if intensity < 5.0:
        result = 'Little or no damage'
    elif intensity < 5.5:
        result = 'Some damage'
    elif intensity < 6.5:
        result = 'Serious damage: walls may crack or fall'
    elif intensity < 7.5:
        result = 'Disaster: buildings may collapse'
    else:
        result = 'Catastrophe: most buildings destroyed'
    return result


def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (float)
        y - y coordinate on a Cartesian plane (float)
    Returns:
        location - quadrant, axis, or origin of coordinate x, y (str)
    -------------------------------------------------------
    """
    if x > 0 and y > 0:
        location = "Quadrant 1"
    elif x < 0 and y > 0:
        location = "Quadrant 2"
    elif x < 0 and y < 0:
        location = "Quadrant 3"
    elif x > 0 and y < 0:
        location = "Quadrant 4"
    elif x == 0 and y != 0:
        location = "Y-Axis"
    elif x != 0 and y == 0:
        location = "X-Axis"
    else:
        location = "Origin"
    return location


def pay_raise(status, years, salary):
    """
    -------------------------------------------------------
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time >= 10 years service
        1.5% for full time < 4 years service
        3% for part time > 10 years service
        1% for part time < 4 years service
        2% for all others
    Use: new_salary = pay_raise(status, years, salary)
    -------------------------------------------------------
    Parameters:
        status - employment type (str - 'F' or 'P')
        years - number of years employed (int > 0)
        salary - current salary (float > 0)
    Returns:
        new_salary - employee's new salary (float).
    -------------------------------------------------------
    """
    if (status == 'F') and (years >= 10):
        new_salary = salary * (1 + FULL_LONG)
    elif (status == 'F') and (years < 4):
        new_salary = salary * (1 + FULL_SHORT)
    elif (status == 'P') and (years > 10):
        new_salary = salary * (1 + PART_LONG)
    elif (status == 'P') and (years < 4):
        new_salary = salary * (1 + PART_SHORT)
    else:
        new_salary = salary * (1 + BASIC_RAISE)
    return new_salary


def loan():
    """
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (bool)
    -------------------------------------------------------
    """
    qualified = False

    years = int(input("Years employed: "))

    if years >= MIN_YEARS:
        salary = float(input("Annual salary: "))

        if salary >= MIN_SALARY:
            qualified = True
    return qualified


def ticket():
    """
    -------------------------------------------------------
    School play ticket price calculation.
    Asks user for their age, and if necessary, if they are
    a student at the school. Prices:
        Infant (age<3): $0
        Senior (age>=65): $4.00
        Student (10<=age<18): $3.00
            Student of this school: $1.00
        Adult (18<=age<65): $5.00
        Kid (3<=age<10): $2.00
    Use: price = ticket()
    -------------------------------------------------------
    Returns:
        price - the price of one ticket (float)
    -------------------------------------------------------
    """
    age = int(input("How old are you? "))

    if age >= SENIOR_AGE:
        price = SENIOR_PRICE
    elif age < INFANT_AGE:
        price = INFANT_PRICE
    elif age >= ADULT_AGE:
        price = ADULT_PRICE
    elif STUDENT_AGE <= age < ADULT_AGE:
        answer = input("Are you a student at this school? (Y/N): ")

        if answer == "Y":
            price = THIS_SCHOOL
        else:
            price = STUDENT_PRICE
    else:
        price = KID_PRICE
    return price


def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
    main = input("Order B - burger or W - wings: ")

    if main == 'B':
        price = BURGER
    else:
        price = WINGS
    combo = input("Make it a combo? (Y/N): ")

    if combo == 'Y':
        side = input("Add F - fries or S - salad: ")

        if side == 'F':
            price += COMBO_F
        else:
            price += COMBO_S
    return price
