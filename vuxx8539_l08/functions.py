"""
-------------------------------------------------------
CP104 List Lab
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from random import randint

DAYS_IN_WEEK = 7
WEEKDAYS = ["Sunday", "Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday"]
MONTHS_PER_YEAR = 12
MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
DIGITS = ["zero", "one", "two", "three", "four",
          "five", "six", "seven", "eight", "nine"]


def get_weekday_name(d):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given its number.
    Use: name = get_weekday_name(d)
    -------------------------------------------------------
    Parameters:
        d - day of week number (1 <= int <= 7)
    Returns:
        name - matching day of the week, 1 = "Sunday", 7 = "Saturday" (str)
    -------------------------------------------------------
    """
    name = WEEKDAYS[d - 1]
    return name


def get_month_name(m):
    """
    -------------------------------------------------------
    Returns the name of a month given its number.
    Use: name = get_month_name(m)
    -------------------------------------------------------
    Parameters:
        m - month number (int 1 <= m <= 12)
    Returns:
        name - matching month, 1 = "January", 12 = "December" (str)
    -------------------------------------------------------
    """
    name = MONTHS[m - 1]
    return name


def get_digit_name(n):
    """
    -------------------------------------------------------
    Returns the name of a digit given its number.
    Use: name = get_digit_name(n)
    -------------------------------------------------------
    Parameters:
        n - digit number (int 0 <= n <= 9)
    Returns:
        name - matching digit, 0 = "zero", 9 = "nine" (str)
    -------------------------------------------------------
    """
    name = DIGITS[n]
    return name


def generate_integer_list(n, low, high):
    """
    -------------------------------------------------------
    Generates a list of random integers.
    (Uses random.randint)
    Use: values = generate_integer_list(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of values to generate (int > 0)
        low - low value range (int)
        high - high value range (int > low)
    Returns:
        values - a list of random integers (list)
    -------------------------------------------------------
    """
    values = []

    for _ in range(n):
        v = randint(low, high)
        values.append(v)
    return values


def get_lotto_numbers(n, low, high):
    """
    -------------------------------------------------------
    Generates a sorted list of unique lottery numbers.
    Requires import: from random import randint
    Use: numbers = get_lotto_numbers(n, low, high)
    -------------------------------------------------------
    Parameters:
        n - number of lottery numbers to generate (int > 0)
        low - low value of the lottery number range (int >= 0)
        high - high value of the lottery number range (int > low)
    Returns:
        numbers - a list of unique random lottery numbers (list of int)
    -------------------------------------------------------
    """
    numbers = []
    i = 0

    while i < n:
        number = randint(low, high)

        if number not in numbers:
            numbers.append(number)
            i += 1
    numbers.sort()
    return numbers


def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics on a list.
    Use: s, l, t, a = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list len(values) > 0)
    Returns:
        smallest - the smallest value in values (float)
        largest - the largest value in values (float)
        total - the total of the numbers in the list (float)
        average - the average value of values (float)
    -------------------------------------------------------
    """
    total = values[0]
    smallest = values[0]
    largest = values[0]

    for v in values[1:]:
        total += v

        if v < smallest:
            smallest = v
        elif v > largest:
            largest = v
    average = total / len(values)
    return smallest, largest, total, average


def list_categorize(values):
    """
    -------------------------------------------------------
    Returns data about the categories of values in a list.
    Use: negatives, positives, zeroes, evens, odds = list_categorize(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns:
        negatives - the number of negative values (int)
        positives - the number of positive values (int)
        zeroes - the number of zeroes (int)
        evens - the number of even values (int)
        odds - the number of odd values (int)
    -------------------------------------------------------
    """
    negatives = 0
    zeroes = 0
    positives = 0
    evens = 0
    odds = 0

    for v in values:
        if v < 0:
            negatives += 1
        elif v > 0:
            positives += 1
        else:
            zeroes += 1
        if v % 2 == 0:
            evens += 1
        else:
            odds += 1
    return negatives, positives, zeroes, evens, odds


def linear_search(a, v):
    """
    -------------------------------------------------------
    Searches through a for the value v and returns its index.
    User: index = linear_search(a, v)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of ?).
        v - can be compared to values in a (?).
    Returns:
        index - the index of the location of v in a, -1 if not found (int).
    -------------------------------------------------------
    """
    n = len(a)
    index = 0

    while index < n and a[index] != v:
        index = index + 1

    if index == n:
        # Value not found.
        index = -1
    return index


def many_search(a, v):
    """
    -------------------------------------------------------
    Searches through a for the value v and returns a list of
    all indexes of its occurrence.
    User: indexes = many_search(a, v)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of ?).
        v - can be compared to values in a (?).
    Returns:
        indexes - a list of indexes of the location of v in a,
            [] if not found (list of int).
    -------------------------------------------------------
    """
    indexes = []

    for i in range(len(a)):
        if a[i] == v:
            indexes.append(i)
    return indexes


def min_search(a):
    """
    -------------------------------------------------------
    Searches through a for the minimum value(s) and returns a
    list of the indexes of those values. (Assumes a has at least
    one element.)
    User: indexes = min_search(a, v)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of ?).
    Returns:
        indexes - a list of indexes of the minimum values in
            a (list of int).
    -------------------------------------------------------
    """
    minval = a[0]
    indexes = [0]

    for i in range(1, len(a)):

        if a[i] < minval:
            minval = a[i]
            indexes = [i]
        elif a[i] == minval:
            indexes.append(i)
    return indexes


def dot_product(source1, source2):
    """
    -------------------------------------------------------
    Calculates a dot product of two lists. Lists must be the
    same length.
    Use: target = dot_product(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - source1 • source2 [source1 dot product source2] (list of float)
    -------------------------------------------------------
    """
    target = 0
    n = len(source1)

    for i in range(n):
        target += source1[i] * source2[i]
    return target


def list_sums(source1, source2):
    """
    -------------------------------------------------------
    Calculates sums of elements of two lists. Lists must be the
    same length.
    Use: target = list_sum(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - sums of elements of source1 and source2 (list of float)
    -------------------------------------------------------
    """
    target = []
    n = len(source1)

    for i in range(n):
        target.append(source1[i] + source2[i])
    return target


def union(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the union of the contents of source1 and source2.
    Every element that appears at least once in either source1 and source2
    must appear once and only once in target.
    Use: target = union(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of ?)
        source2 - a list (list of ?)
    Returns:
        target - the union of source1 and source2 (list of ?)
    -------------------------------------------------------
    """
    target = []

    for v in source1:
        if v not in target:
            target.append(v)
    for v in source2:
        if v not in target:
            target.append(v)
    return target


def intersection(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the intersection of the contents of source1 and source2.
    Only elements that appear in both source1 and source2
    appear once and only once in target.
    Use: target = intersection(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of ?)
        source2 - a list (list of ?)
    Returns:
        target - the intersection of source1 and source2 (list of ?)
    -------------------------------------------------------
    """
    target = []

    for v in source1:
        if v in source2 and v not in target:
            target.append(v)
    return target


def symmetric_difference(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the symmetric difference of the contents
    of source1 and source2.
    Only elements that appear in one of source1 and source2
    appear once and only once in target.
    Use: target = symmetric_difference(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of ?)
        source2 - a list (list of ?)
    Returns:
        target - the symmetric difference of source1 and source2 (list of ?)
    -------------------------------------------------------
    """
    target = []

    for v in source1:
        if v not in source2 and v not in target:
            target.append(v)
    for v in source2:
        if v not in source1 and v not in target:
            target.append(v)
    return target
