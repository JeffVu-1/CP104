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
RETIREMENT = 65

WEEKS = 6


def sum_even(num):
    """
    -------------------------------------------------------
    Sums and returns all even numbers from 2 to num (inclusive).
    Use: total = sum_even(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all even numbers from 2 to num (int)
    ------------------------------------------------------
    """
    total = 0

    for i in range(2, num + 1, 2):
        total += i
    return total


def sum_odd(num):
    """
    -------------------------------------------------------
    Sums and returns all odd numbers from 1 to num (inclusive).
    Use: total = sum_odd(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all odd numbers from 1 to num (int)
    ------------------------------------------------------
    """
    total = 0

    for i in range(1, num + 1, 2):
        total += i
    return total


def sum_all(start, finish, increment):
    """
    -------------------------------------------------------
    Sums and returns all odd numbers from start to finish (inclusive)
    by increment.
    Use: total = sum_all(start, finish, increment)
    -------------------------------------------------------
    Parameters:
        start - an integer (int > 0)
        finish - an integer (int >= start)
        increment - an integer (int > 0)
    Returns:
        total - sum of all odd numbers from start to
            finish by increment (int)
    ------------------------------------------------------
    """
    total = 0

    for i in range(start, finish + 1, increment):
        total += i
    return total


def sum_partial_harmonic(n):
    """
    -------------------------------------------------------
    Sums and returns the total of a partial harmonic series.
    This series is the sum of all terms 1/i, where i ranges
    from 1 to n (inclusive).
    i.e. 1 + 1/2 + 1/3 + ... + 1/n
    Use: total = sum_partial_harmonic(n)
    -------------------------------------------------------
    Parameters:
        n - an integer (int > 0)
    Returns:
        total - sum of partial harmonic series from 1 to n (int)
    ------------------------------------------------------
    """
    total = 0

    for i in range(1, n + 1):
        total += 1 / i
    return total


def draw_rectangle(height, width, char):
    """
    -------------------------------------------------------
    Prints a rectangle of height and width characters using
    the char character.
    Use: draw_rectangle(height, width, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int &gt; 0)
        width - number of characters wide (int &gt; 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for _ in range(height):
        print(char * width)
    return


def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(height):
        print(" " * (height - i - 1), end="")
        print(char * (i * 2 + 1))
    return


def draw_hollow_triangle(width, char):
    """
    -------------------------------------------------------
    Prints a hollow triangle of width characters using
    the char character.
    Use: draw_hollow_triangle(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    print(char)

    if width > 1:
        for i in range(width - 2):
            print("{}{}{}".format(char, " " * i, char))

        for i in range(width):
            print("{}".format(char), end="")
    print()
    return


def draw_arrow(width, char):
    """
    -------------------------------------------------------
    Prints a triangle of width characters using
    the char character.
    Use: draw_triangle(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(1, width):
        print(char * i)
    for i in range(width, -1, -1):
        print(char * i)
    print()
    return


def statistics(n):
    """
    -------------------------------------------------------
    Asks a user to enter n values, then calculates and returns
    the minimum, maximum, total, and average of those values.
    Use: minimum, maximum, total, average = statistics(n)
    -------------------------------------------------------
    Parameters:
        n - number of values to process (int > 0)
    Returns:
        minimum - smallest of n values (float)
        maximum - largest of n values (float)
        total - total of n values (float)
        average - average of n values (float)
    ------------------------------------------------------
    """
    value = float(input("First value: "))
    minimum = value
    maximum = value
    total = value

    for _ in range(1, n):
        value = float(input("Next value: "))
        total = total + value

        if value < minimum:
            minimum = value
        elif value > maximum:
            maximum = value

    average = total / n
    return minimum, maximum, total, average


def bottles_of_beer(verses):
    """
    -------------------------------------------------------
    Prints the verses of the old song "99 Bottles of Beer on the Wall".
    Use: bottles_of_beer(verses)
    -------------------------------------------------------
    Parameters:
        verses - number of verses to print (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for quantity in range(verses, 2, -1):
        print("{0} bottles of beer on the wall, {0} bottles of beer."
              .format(quantity))
        print("Take one down, pass it around, {0} bottles of beer on the wall."
              .format(quantity - 1))
        print("--")

    print("{} bottles of beer on the wall, {} bottles of beer.".format(2, 2))
    print("Take one down, pass it around, {} bottle of beer on the wall."
          .format(1))
    print("--")
    print("{} bottle of beer on the wall, {} bottle of beer.".format(1, 1))
    print("Take one down, pass it around, no more bottles of beer on the wall!")
    print("--")
    return


def treadmill(burnt_per_minute, start, end, inc):
    """
    -------------------------------------------------------
    Calculates and prints calories burnt on a treadmill over
    a given time range.
    Use: treadmill(burnt_per_minute, start, end, inc)
    -------------------------------------------------------
    Parameters:
        burnt_per_minute - calories burnt per minute (float > 0)
        start - start time in minutes (int > 0)
        end - end time in minutes (int >= start)
        inc - increment in minutes (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for minutes in range(start, end + 1, inc):
        burnt = burnt_per_minute * minutes
        print("Calories burned after {} minutes: {:.1f}".format(minutes, burnt))
    return


def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates a prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """
    rate = 1 + increase / 100

    print()
    print("Age         Salary")
    print("------------------")

    for year in range(age, RETIREMENT + 1):
        print("{:2d} {:15,.2f}".format(year, salary))
        salary = salary * rate
    return


def gic(value, years, rate):
    """
    -------------------------------------------------------
    Calculates a prints a table of how much a GIC (Guaranteed
    Income Certificate) is worth over a number of years, and
    returns its final value.
    Use: final_value = gic(value, years, rate)
    -------------------------------------------------------
    Parameters:
        value - GICs initial value (int > 0)
        years - number of years to maturity (int > 0)
        rate - percent increase value per year (float > 0)
    Returns:
        final_value - the final value of the GIC (float)
    ------------------------------------------------------
    """
    rate = 1 + rate / 100
    final_value = value

    print()
    print("Year       Value $")
    print("------------------")
    print("{:2d} {:15,.2f}".format(0, final_value))

    for year in range(1, years + 1):
        final_value = final_value * rate
        print("{:2d} {:15,.2f}".format(year, final_value))
    return final_value


def ia_hours(ia_count):
    """
    -------------------------------------------------------
    Calculates the total number of hours that IAs (Instructional
    Assistants) work over a 6 week period by asking for the hours
    for each IA per week.
    Use: total_hours = ia_hours(ia_count)
    -------------------------------------------------------
    Parameters:
        ia_count - number of IAs (int > 0)
    Returns:
        total_hours - hours worked by all IAs (float)
    ------------------------------------------------------
    """
    total_hours = 0

    for week in range(1, WEEKS + 1):
        print("Week {}".format(week))

        for ia in range(1, ia_count + 1):
            time = float(input("  Marking hours for IA {}: ".format(ia)))
            total_hours += time
    return total_hours


def lumber(b_min, b_max, b_inc, h_min, h_max, h_inc):
    """
    -------------------------------------------------------
    Create a table of the engineering properties of its lumber.
    Given the base and height of a piece of lumber in inches,
    different properties of a piece of lumber are calculated as:
        cross-sectional area = base × height
        moment of inertia = base × height^3 / 12
        section modulus = base × height^2 / 6
    Use: lumber(b_min, b_max, b_inc, h_min, h_max, h_inc)
    -------------------------------------------------------
    Parameters:
        b_min - minimum value of base (int > 0)
        b_max - maximum value of base (int > b_min)
        b_inc - increment in base value (int > 0)
        h_min - minimum value of height (int > 0)
        h_max - maximum value of height (int > h_min)
        h_inc - increment in height value (int > 0)
    Returns:
        total_hours - hours worked by all IAs (float)
    ------------------------------------------------------
    """
    print("              Cross-Sectional  Moment of  Section")
    print("Base  Height  Area             Inertia    Modulus")
    print()

    for base in range(b_min, b_max + 1, b_inc):
        for height in range(h_min, h_max + 1, h_inc):
            csa = base * height
            moi = base * height ** 3 / 12.0
            mod = base * height ** 2 / 6.0
            print("{:4d}  x {:4d}  {:15.2f}  {:9.2f}  {:7.2f}"
                  .format(base, height, csa, moi, mod))
    return
