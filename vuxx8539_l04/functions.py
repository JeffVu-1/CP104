"""
-------------------------------------------------------
Lab 4 - Functions
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from math import pi

FAHRENHEIT_FREEZING = 32
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = SECONDS_PER_MINUTE * 60
SECONDS_PER_DAY = SECONDS_PER_HOUR * 24
DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MINUTES_PER_HOUR = 60
SECONDS_PER_YEAR = DAYS_PER_YEAR * HOURS_PER_DAY * \
    MINUTES_PER_HOUR * SECONDS_PER_MINUTE

def diameter(radius):
    """
    -------------------------------------------------------
    Calculates and returns diameter of a circle.
    Use: diam = diameter(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        diam - diameter of a circle (float)
    ------------------------------------------------------
    """
    diam = 2 * radius
    return diam


def circumference(radius):
    """
    -------------------------------------------------------
    Calculates and returns circumference of a circle.
    Use: c = circumference(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        c - circumference of a circle (float)
    ------------------------------------------------------
    """
    c = 2 * pi * radius
    return c


def area(radius):
    """
    -------------------------------------------------------
    Calculates and returns area of a circle.
    Use: a = area(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        a - area of a circle (float)
    ------------------------------------------------------
    """
    a = pi * radius ** 2
    return a


def square_pyramid(base, height):
    """
    -------------------------------------------------------
    Calculates and returns the slant height, area, and
    volume of a square pyramid given the base and perpendicular
    height.
    Use: sh, a, v = square_pyramid(base, height)
    -------------------------------------------------------
    Parameters:
        base - length of the base of the pyramid (float > 0)
        height - perpendicular height of the pyramid (float > 0)
    Returns:
        sh - slant height of the square pyramid (float)
        a - area of the square pyramid (float)
        v - volume of the square pyramid (float)
    ------------------------------------------------------
    """
    sh = ((base / 2)**2 + height**2)**0.5
    a = base**2 + 2 * base * (base**2 / 4 + height**2)**0.5
    v = base**2 * height / 3
    return sh, a, v


def right_triangle(adjacent, opposite):
    """
    -------------------------------------------------------
    Calculates and returns the hypotenuse, circumference, and
    area of a right triangle given two non-hypotenuse sides.
    Use: h, c, a = triangle(adjacent, opposite)
    -------------------------------------------------------
    Parameters:
        adjacent - length of side right triangle (float > 0)
        opposite - length of side right triangle (float > 0)
    Returns:
        h - hypotenuse of the triangle (float)
        c - circumference of the triangle (float)
        a - area of the triangle (float)
    ------------------------------------------------------
    """
    h = (adjacent**2 + opposite**2)**0.5
    c = adjacent + opposite + h
    a = 0.5 * adjacent * opposite
    return h, c, a


def pythag(s1, s2):
    """
    -------------------------------------------------------
    Calculates and returns the radius, diameter, circumference,
    and area of circle defined by a right triangle.
    Use: r, d, c, a = python(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - length of side 1 of a right triangle (float > 0)
        s2 - length of side 2 of a right triangle (float > 0)
    Returns:
        r - radius of the resulting circle (float)
        d - diameter of the resulting circle (float)
        c - circumference of the resulting circle (float)
        a - area of the resulting circle (float)
    ------------------------------------------------------
    """
    # Calculate radius based upon the hypotenuse of the triangle
    r = (s1**2 + s2**2) ** 0.5
    d = r * 2
    c = 2 * pi * r
    a = pi * r**2
    return r, d, c, a


def total_change(nickels, dimes, quarters, loonies, toonies):
    """
    -------------------------------------------------------
    Calculates the total value of a set of coins in dollars.
    Each coin is worth:
        nickel:  $0.05
        dime:    $0.10
        quarter: $0.25
        loonie:  $1.00
        toonie:  $2.00
    Use: total = total_change(nickels, dimes, quarters, loonies, toonies)
    -------------------------------------------------------
    Parameters:
        nickels - number of nickels (int >= 0)
        dimes - number of dimes (int >= 0)
        quarters - number of quarters (int >= 0)
        loonies - number of loonies (int >= 0)
        toonies - number of toonies (int >= 0)
    Returns:
        total - total value of coins (float)
    -------------------------------------------------------
    """
    assert nickels >= 0, "nickels must be >= 0"
    assert dimes >= 0, "dimes must be >= 0"
    assert quarters >= 0, "quarters must be >= 0"
    assert loonies >= 0, "loonies must be >= 0"
    assert toonies >= 0, "toonies must be >= 0"

    NICKEL = 5
    DIME = 10
    QUARTER = 25
    LOONIE = 100
    TOONIE = 200

    total = nickels * NICKEL + dimes * DIME + quarters * \
        QUARTER + loonies * LOONIE + toonies * TOONIE
    return total / 100


def computer_costs(computer_cost, computers_bought, commission_percent):
    """
    -------------------------------------------------------
    Calculates purchase costs of computers
    Use: pre_commission_cost, total_cost = computer_costs(computer_cost,
        computers_bought, commission_percent)
    -------------------------------------------------------
    Parameters:
        computer_cost - per unit cost (float >= 0)
        computers_bought - units bought (int >= 0)
        commission_percent - wholesaler commission (float >= 0)
    Returns:
        pre_commission_cost - cost before commission (float)
        total_cost - cost after commission (float)
    -------------------------------------------------------
    """
    assert computer_cost >= 0, "computer cost must be >= 0"
    assert computers_bought >= 0, "computers bought must be >= 0"
    assert commission_percent >= 0, "commission percent must be >= 0"

    pre_commission_cost = computer_cost * computers_bought
    total_cost = pre_commission_cost * (1 + commission_percent / 100)
    return pre_commission_cost, total_cost


def fraction_product(num1, den1, num2, den2):
    """
    -------------------------------------------------------
    Calculates and returns fraction values.
    Use: num, den, product = fraction_product(num1, den1, num2, den2)
    -------------------------------------------------------
    Parameters:
        num1 - numerator of first fraction (int)
        den1 - denominator of first fraction (int != 0)
        num2 - numerator of second fraction (int)
        den2 - denominator of second fraction (int != 0)
    Returns:
        num - numerator of product (int)
        den - denominator of product (int)
        product - num / den (float)
    -------------------------------------------------------
    """
    assert den1 != 0, "denominator 1 cannot be 0"
    assert den2 != 0, "denominator 2 cannot be 0"

    num = num1 * num2
    den = den1 * den2
    product = num / den
    return num, den, product


def population(size, births, deaths, immigrants, years):
    """
    -------------------------------------------------------
    Calculates future population given various factors.
    Use: new_size = population(size, births, deaths, immigrants, years)
    -------------------------------------------------------
    Parameters:
       size - current population (int >= 0)
       births - average seconds between births (int >= 0)
       deaths - average seconds between deaths (int >= 0)
       immigrants - average seconds between immigrations (int >= 0)
       years - years to calculate new population (int > 0)
    Returns:
       new_size - new population size (int)
    -------------------------------------------------------
    """
    assert size >= 0, "current population must be >= 0"
    assert births >= 0, "births must be >= 0"
    assert deaths >= 0, "deaths must be >= 0"
    assert immigrants >= 0, "immigrants must be >= 0"
    assert years > 0, "number of years must be > 0"

    total_seconds = SECONDS_PER_YEAR * years
    total_births = total_seconds // births
    total_deaths = total_seconds // deaths
    total_immigrants = total_seconds // immigrants
    new_size = size + total_births - total_deaths + total_immigrants
    return new_size


def slope(x1, y1, x2, y2):
    """
    -------------------------------------------------------
    Calculates the slope of a line. Slope is calculated as
    rise / run, where rise is distance between y coordinates,
    and run is distance between x coordinates.
    Use: s = slope(x1, y1, x2, y2)
    -------------------------------------------------------
    Parameters:
        x1 - x coordinate of first point on a graph (float)
        y1 - y coordinate of first point on a graph (float)
        x2 - x coordinate of second point on a graph (float)
        y2 - y coordinate of second point on a graph (float)
        x2 != x1
    Returns:
        s - slope of the line through (x1,y1) and (x2,y2)
    -------------------------------------------------------
    """
    assert x2 - x1 != 0, "x2 - x1 cannot be 0"

    run = x2 - x1
    rise = y2 - y1
    s = rise / run
    return s


def c_to_f(celsius):
    """
    -------------------------------------------------------
    Converts temperatures in celsius to fahrenheit.
    Use: fahrenheit = c_to_f(celsius)
    -------------------------------------------------------
    Parameters:
        celsius - temperature in celsius (int >= -273)
    Returns:
        fahrenheit - equivalent to celsius (float)
    -------------------------------------------------------
    """
    fahrenheit = 9.0 / 5.0 * celsius + FAHRENHEIT_FREEZING
    return fahrenheit


def f_to_c(fahrenheit):
    """
    -------------------------------------------------------
    Converts temperatures in fahrenheit to celsius.
    Use: celsius = f_to_c(fahrenheit)
    -------------------------------------------------------
    Parameters:
        fahrenheit - temperature in fahrenheit (int >= -459)
    Returns:
        celsius - equivalent to celsius (float)
    -------------------------------------------------------
    """
    celsius = (fahrenheit - FAHRENHEIT_FREEZING) * 5.0 / 9.0
    return celsius


def time_values(seconds):
    """
    -------------------------------------------------------
    Returns total_seconds in different formats.
    Use: days, hours, minutes = time_values(seconds)
    -------------------------------------------------------
    Parameters:
        seconds - total seconds (int >= 0)
    Returns:
        days - number of days in total_seconds (int >= 0)
        hours - number of hours in total_seconds (int >= 0)
        minutes - number of minutes in total_seconds (int >= 0)
    -------------------------------------------------------
    """
    assert seconds >= 0, "Total seconds must be >= 0"
    days = seconds // SECONDS_PER_DAY
    hours = seconds // SECONDS_PER_HOUR
    minutes = seconds // SECONDS_PER_MINUTE
    return days, hours, minutes


def time_split(initial_seconds):
    """
    -------------------------------------------------------
    Converts total seconds into days, hours, minutes, and seconds.
    Use: d, h, m, s = time_split(initial_seconds)
    -------------------------------------------------------
    Parameters:
        initial_seconds - time elapsed (int >= 0)
    Returns:
        days - number of days in initial_seconds (int)
        hours - remaining hours in initial_seconds (int)
        minutes - remaining minutes in initial_seconds (int)
        seconds - remaining seconds in initial_seconds (int)
    -------------------------------------------------------
    """
    assert initial_seconds >= 0, "seconds must be >= 0"

    days = int(initial_seconds // SECONDS_PER_DAY)
    seconds = initial_seconds % SECONDS_PER_DAY
    hours = int(seconds // SECONDS_PER_HOUR)
    seconds = seconds % SECONDS_PER_HOUR
    minutes = int(seconds // SECONDS_PER_MINUTE)
    seconds = seconds % SECONDS_PER_MINUTE
    return days, hours, minutes, seconds
