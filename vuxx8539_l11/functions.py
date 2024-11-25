"""
-------------------------------------------------------
Lab - Two-D Lists
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
from random import randint, uniform

DIGITS = '0123456789'
PUNCTUATION = ".?!"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []

    for _ in range(rows):
        row = []

        for _ in range(cols):
            if value_type == "float":
                value = uniform(low, high)
            else:
                value = randint(low, high)
            row.append(value)
        matrix.append(row)
    return matrix


def generate_matrix_char(rows, cols):
    """
    -------------------------------------------------------
    Generates a 2D list of random lower case letter ('a' - 'z') values
    Use: matrix = generate_matrix_char(rows, cols)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the generated matrix (int > 0)
        cols - number of columns in the generated matrix (int > 0)
    Returns:
        matrix - a 2D list of random characters (2D list of str)
    -------------------------------------------------------
    """
    charmatrix = []

    for _ in range(rows):
        row = []

        for _ in range(cols):
            index = randint(0, 25)
            row.append(ALPHABET[index])
        charmatrix.append(row)
    return charmatrix


def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    rows = len(matrix)
    cols = len(matrix[0])

    print("  ", end='')
    for i in range(cols):
        print("{:7}".format(i), end='')
    print()
    for i in range(rows):
        print("{:2}".format(i), end='')

        for j in range(cols):
            if value_type == "float":
                print("{:7.2f}".format(matrix[i][j]), end='')
            else:
                print("{:7}".format(matrix[i][j]), end='')
        print()
    return


def print_matrix_char(matrix):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
    Use: print_matrix_char(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of strings (2D list)
    Returns:
        None.
    -------------------------------------------------------
    """
    rows = len(matrix)
    cols = len(matrix[0])

    print("  ", end='')
    for i in range(cols):
        print("{:5}".format(i), end='')
    print()
    for i in range(rows):
        print("{:2}".format(i), end='')

        for j in range(cols):
            print("{:>5}".format(matrix[i][j]), end='')
        print()
    return


def words_to_matrix(word_list):
    """
    -------------------------------------------------------
    Generates a 2D list of character values from the given
    list of words. All words must be the same length.
    Use: matrix = words_to_matrix(word_list)
    -------------------------------------------------------
    Parameters:
        word_list - a list containing the words to be placed in
            the matrix (list of string)
    Returns:
        matrix - a 2D list of characters of the given words
         in word_list (2D list of string).
    -------------------------------------------------------
    """
    matrix = []

    for word in word_list:
        row = []

        for char in word:
            row.append(char)
        matrix.append(row)
    return matrix


def stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
    Use: smallest, largest, total, average = stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    smallest = matrix[0][0]
    largest = matrix[0][0]
    total = 0

    for i in range(len(matrix)):

        for j in range(len(matrix[i])):

            if matrix[i][j] > largest:
                largest = matrix[i][j]
            elif matrix[i][j] < smallest:
                smallest = matrix[i][j]
            total += matrix[i][j]
    average = total / (len(matrix) * len(matrix[0]))
    return smallest, largest, total, average


def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """
    smallest = matrix[0][0]
    largest = matrix[0][0]
    s_loc = [0, 0]
    l_loc = [0, 0]

    for i in range(len(matrix)):

        for j in range(len(matrix[i])):

            if matrix[i][j] > largest:
                largest = matrix[i][j]
                l_loc = [i, j]
            elif matrix[i][j] < smallest:
                smallest = matrix[i][j]
                s_loc = [i, j]
    return s_loc, l_loc


def find_less(matrix, n):
    """
    -------------------------------------------------------
    Finds the location [row, column] of the first value in matrix
    that is smaller than a target value, n. If there is no such
    number in matrix, it should return an empty list.
    Use: loc = find_less(matrix, n)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
        n - the target value (float)
    Returns:
        loc - a list of the row and column location of
            the the first value smaller than n in values,
            an empty list otherwise (list of int)
    -------------------------------------------------------
    """
    loc = []
    rows = len(matrix)
    cols = len(matrix[0])
    i = 0

    while i < rows and loc == []:
        j = 0

        while j < cols and loc == []:
            if matrix[i][j] < n:
                loc = [i, j]
            j += 1
        i += 1
    return loc


def count_frequency(matrix, c):
    """
    -------------------------------------------------------
    Count the number of appearances of the given character char
    in matrix.
    Use: count = count_frequency(matrix, char)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to search in it (2D list of str)
        char - character to search for it (str, len = 1)
    Returns:
        count - the number of appearances of char in the matrix (int)
    -------------------------------------------------------
    """
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == c:
                count += 1
    return count


def find_word_horizontal(matrix, word):
    """
    -------------------------------------------------------
    Look for word in each row of the given matrix of characters.
    Returns a list of indexes of all rows that are equal to word.
    Returns an empty list if no row is equal to word.
    Use: rows = find_word_horizontal(matrix, word)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix of characters (2D list of str)
        word - the word to search for (str)
    Returns:
        rows - a list of row indexes (list of int)
    ------------------------------------------------------
    """
    rows = []
    n = len(word)
    m = len(matrix[0])

    if m == n:

        for r in range(len(matrix)):
            c = 0

            while c < m and matrix[r][c] == word[c]:
                c += 1

            if c == m:
                rows.append(r)
    return rows


def find_word_vertical(matrix, word):
    """
    -------------------------------------------------------
    Look for word in each column of the given matrix of characters.
    Returns a list of indexes of all column that are equal to word.
    Returns an empty list if no column is equal to word.
    Use: cols = find_word_vertical(matrix, word)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix of characters (2D list of str)
        word - the word to search for (str)
    Returns:
        cols - a list of column indexes (list of int)
    ------------------------------------------------------
    """
    cols = []
    n = len(word)
    m = len(matrix)

    if m == n:

        for c in range(len(matrix[0])):
            r = 0

            while r < m and matrix[r][c] == word[r]:
                r += 1

            if r == m:
                cols.append(c)
    return cols


def find_word_diagonal(matrix, word):
    """
    -------------------------------------------------------
    Returns whether word is on the diagonal of a square matrix
    of characters.
    Use: found = find_word_diagonal(matrix, word)
    -------------------------------------------------------
    Parameters:
        matrix - a 2d list of characters (2d list of str)
        word - the word to compare against the diagonal of matrix (str)
    Returns:
        found - True if word is on the diagonal of matrix,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    m = len(matrix)
    n = len(word)
    found = False

    if n == m:
        i = 0

        while i < m and matrix[i][i] == word[i]:
            i += 1

        if i == m:
            found = True
    return found


def scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = num * matrix[i][j]
    return


def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of ?)
    Returns:
        b - the transposed matrix (2D list of ?)
    ------------------------------------------------------
    """
    b = []
    rows = len(a)
    cols = len(a[0])

    for j in range(cols):
        row = []

        for i in range(rows):
            row.append(a[i][j])
        b.append(row)
    return b


def matrix_equal(matrix1, matrix2):
    """
    -------------------------------------------------------
    Compares two matrices to see if they are equal - i.e. have the
    same contents in the same locations.
    Use: equal = matrix_equal(matrix1, matrix2)
    -------------------------------------------------------
    Parameters:
        matrix1 - the first matrix (2D list of ?)
        matrix2 - the second matrix (2D list of ?)
    Returns:
        equal - True if matrix1 and matrix2 are equal,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if (rows1 == rows2) and (cols1 == cols2):
        equal = True
        i = 0

        while equal and i < rows1:
            j = 0

            while j < cols1 and matrix1[i][j] == matrix2[i][j]:
                j += 1

            if j < cols1:
                equal = False
            else:
                i += 1
    else:
        equal = False
    return equal


def matrix_distinct_values(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of  unique numbers of type float or int.
    Use: matrix = matrix_distinct_values(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of unique values (list of int/float)
    -------------------------------------------------------
    """
    matrix = []
    used_values = []

    for _ in range(rows):
        row = []
        j = 0

        while j < cols:
            if value_type == "float":
                val = uniform(low, high)

                while val in matrix:
                    val = uniform(low, high)
            else:
                found = True

                while found:
                    val = randint(low, high)

                while val in matrix:
                    val = randint(low, high)

            used_values.append(val)
            row.append(val)
            j += 1
        matrix.append(row)
    return matrix
