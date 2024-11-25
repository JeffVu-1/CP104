"""
-------------------------------------------------------
Lab 7 Functions
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
VOWELS = "aeiou"
ALL_VOWELS = "aeiouAEIOU"

def is_hydroxide(chemical):
    """
    -------------------------------------------------------
    Determines if a chemical formula is a hydroxide.
    Use: hydroxide = is_hydroxide(chemical)
    -------------------------------------------------------
    Parameters:
        chemical - a chemical formula (str)
    Returns:
        hydroxide - True if chemical is a hydroxide (ends in 'OH'),
            False otherwise (boolean)
    -------------------------------------------------------
    """
    n = len(chemical)

    if chemical[n - 2:] == 'OH':
        hydroxide = True
    else:
        hydroxide = False
    return hydroxide


def is_hydroxide_2(chemical):
    """
    Alternative
    """
    if chemical[-2:] == 'OH':
        hydroxide = True
    else:
        hydroxide = False
    return hydroxide


def is_hydroxide_3(chemical):
    """
    Alternative
    """
    return chemical.endswith('OH')


def url_categorize(url):
    """
    -------------------------------------------------------
    Returns whether a url represents a business, a non-profit, or another
    type of organization.
    Use: url_type = org_categorize(url)
    -------------------------------------------------------
    Parameters:
        url - the web address of the organization (str)
    Returns:
        url_type - the organization type (str)
            'business' if url ends with 'com'
            'non-profit' if url ends with 'org'
            'other' if url ends with something else
    ------------------------------------------------------
    """
    if url.endswith('com'):
        url_type = 'business'
    elif url.endswith('org'):
        url_type = 'non-profit'
    else:
        url_type = 'other'
    return url_type


def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    pc = product_code[:3]
    pi = product_code[3:7]
    pq = product_code[7:]
    return pc, pi, pq


def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        None
    -------------------------------------------------------
    """
    pc, pid, pq = parse_code(product_code)

    if len(pc) == 3 and pc.isalpha() and pc.isupper():
        print("Category {0} is valid.".format(pc))
    else:
        print("Category {0} is not valid.".format(pc))

    if len(pid) == 4 and pid.isdigit():
        print("ID {0} is valid.".format(pid))
    else:
        print("ID {0} is not valid.".format(pid))

    if len(pq) > 0 and pq[0].isupper():
        print("Qualifier {0} is valid.".format(pq))
    else:
        print("Qualifier {0} is not valid.".format(pq))
    return


def password_strength(password):
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
        not long enough - if password less than 8 characters
        no digits - if password has no digits
        no upper case - if password has no upper case letters
        no lower case - if password has no lower case letters
    Use: passwd_strength(pass)
    -------------------------------------------------------
    Parameters:
        password - the password to be checked (str)
    Returns:
        None
    ------------------------------------------------------
    """
    if len(password) < 8:
        print("not long enough")

    digits = 0
    upper = 0
    lower = 0

    for c in password:
        if c.isdigit():
            digits += 1
        if c.isupper():
            upper += 1
        if c.islower():
            lower += 1

    if digits == 0:
        print("no digits")
    if upper == 0:
        print("no upper case")
    if lower == 0:
        print("no lower case")
    return


def is_palindrome(s):
    """
    -----------------------------------------------------------------
    Checks whether the given string is palindrome or not. A palindrome is
    a string the reads the same forwards as backwards.
    Use: palindrome = is_palindrome(s)
    -----------------------------------------------------------------
    Parameters:
        s - a string to be checked (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -----------------------------------------------------------------
    """
    palindrome = True

    i = 0
    n = len(s) - 1
    mid = n // 2

    while i < mid and s[i] == s[n]:
        i += 1
        n -= 1

    if i < mid:
        palindrome = False

    return palindrome


def vowel_count(s):
    """
    -------------------------------------------------------
    Counts the number of vowels in a string. Does not include 'y'.
    Use: count = vowel_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of vowels in s (int)
    -------------------------------------------------------
    """
    count = 0

    for c in s.lower():
        if c in VOWELS:  # Look for c in list of vowels.
            count = count + 1
    return count


def digit_count(s):
    """
    -------------------------------------------------------
    Counts the number of digits in a string.
    Use: count = digit_count(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - the number of digits in s (int)
    -------------------------------------------------------
    """
    count = 0

    for c in s:
        if c.isdigit():
            count = count + 1
    return count


def count_special_chars(s):
    """
    -------------------------------------------------------
    Counts the number of special characters in s.
    The special characters are: "#", "@", "$", "%", "&", "!".
    Use: count = count_special_chars(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        count - number of special characters in s (int)
    ------------------------------------------------------
    """
    count = 0

    for c in s:
        if c in "#@$%&!":
            count = count + 1
    return count


def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (int >= 0)
    ------------------------------------------------------
    """
    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0

    for v in txt:
        if v.isdigit():
            dgts += 1
        elif v.isupper():
            uppr += 1
        elif v.islower():
            lowr += 1
        elif v.isspace():
            whtspc += 1

    return uppr, lowr, dgts, whtspc


def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. Returns a copy of s with all the vowels
    removed. Y is not treated as a vowel. Preserves case.
    Use: out = dsmvwl(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        out - s with its vowels removed (str)
    -------------------------------------------------------
    """
    out = ''

    for c in s:
        if c.lower() not in VOWELS:
            # Concatenates only non-vowels to the return string.
            out += c
    return out


def dsmvwl_2(s):
    """
    Alternative
    """
    for c in ALL_VOWELS:
        s = s.replace(c, "")
    return s


def comma_period_replace(s):
    """
    -------------------------------------------------------
    Replaces all the commas with a period in s.
    Use: out = comma_period_replace(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        out - s with all commas replaced by a period (str)
    ------------------------------------------------------
    """
    out = ""

    for c in s:
        if c == ",":
            out += "."
        else:
            out += c

    return out


def total_digits(s):
    """
    -------------------------------------------------------
    Extracts and calculates the total of all digits in s.
    Use: total = total_digits(s)
    -------------------------------------------------------
    Parameters:
        s - a string (str)
    Returns:
        total - total of all the digits in s (int)
    ------------------------------------------------------
    """
    total = 0

    for c in s:
        if c.isdigit():
            total += int(c)
    return total


def str_distance(s1, s2):
    """
    -------------------------------------------------------
    Finds the distance between the s1 and s2. The distance between two
    strings of the same length is the number of positions in the strings
    at which their characters are different. If two strings are not the
    same length, the distance is unknown (-1). If the distance is zero,
    then two strings are equal.
    Use: d = str_distance(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - first string (str)
        s2 - second string (str)
    Returns:
        d - the distance between s1 and s2 (int)
    ------------------------------------------------------
    """
    if len(s1) != len(s2):
        d = -1
    else:
        d = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                d += 1
    return d


def calculate(expr):
    """
    -----------------------------------------------------------------
    Treats expr as a math expression and evaluates it.
    expr must have the following format:
        operand1 operator operand2
    operators are: +, -, *, /, %
    operands are one-digit integer numbers
    Return None if second operand is zero for division.
    Use: result = calculate(expr)
    -----------------------------------------------------------------
    Parameters:
        expr - an arithmetic expression to be calculated (str)
    Returns:
        result - The result of arithmetic expression (float)
    -----------------------------------------------------------------
    """
    op1 = int(expr[0])
    operator = expr[2]
    op2 = int(expr[4])

    if operator == '+':
        result = op1 + op2
    elif operator == '-':
        result = op1 - op2
    elif operator == '*':
        result = op1 * op2
    elif operator == '/':
        if op2 == 0:
            result = None
        else:
            result = op1 / op2
    elif operator == '%':
        if op2 == 0:
            result = None
        else:
            result = op1 % op2
    return result
