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

def file_top(file_handle, count):
    """
    -------------------------------------------------------
    Prints first count lines of file_handle. Line numbering starts at 0.
    If length of file is shorter than count, stops printing after
    last line of file.
    Use: file_top(file_handle, count)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
        count - number of lines to print (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """

    i = 0
    while i < count:
        line = file_handle.readline()
        if line == '':
            break
        else:
            print(line, end="")
        i += 1
    return


def read_integers(file_handle):
    """
    -------------------------------------------------------
    Extracts positive integers from a file into a list of integers.
    Numbers are comma-delimited. Non-numeric tokens are ignored.
    Use: number_list = read_integers(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        number_list - a list of integers from file_handle (list of int)
    -------------------------------------------------------
    """

    number_list = []
    line = file_handle.readline()
    while line != '':
        for tingy in line.split(','):
            if tingy.isdigit():
                number_list.append(int(tingy))
        line = file_handle.readline()
    return number_list


def file_statistics(file_handle):
    """
    -------------------------------------------------------
    Evaluates the contents of a file by counting upper-case letters,
    lower-case letters, digits, white-spaces (inluding end-of-line
    characters), and remaining ccharacters.
    Use: ucount, lcount, dcount, wcount, rcount = file_statistics(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - file to process (file handle - open for reading)
    Returns:
        ucount - The number of upper-case letters in the file (int)
        lcount - The number of lower-case letters in the file (int)
        dcount - The number of digits in the file (int)
        wcount - The number of white-space characters in the file (int)
        rcount - The number of remaining characters in the file (int)
    -------------------------------------------------------
    """

    ucount = 0
    lcount = 0
    dcount = 0
    wcount = 0
    rcount = 0
    line = file_handle.readline()
    while line != '':
        for char in line:
            if char.isupper():
                ucount += 1
            elif char.islower():
                lcount += 1
            elif char.isdigit():
                dcount += 1
            elif char.isspace():
                wcount += 1
            else:
                rcount += 1
        line = file_handle.readline()
    return ucount, lcount, dcount, wcount, rcount


def line_numbering(fh_read, fh_write):
    """
    -------------------------------------------------------
    Adds line numbers to a file. Contents of fh_write contain contents
    of fh_read where every line has line numbers added to the beginning
    of the line in the format [number]. Line numbering starts at 0.
    Put a single space after the line number.
    Use: line_numbering(fh_read, fh_write)
    -------------------------------------------------------
    Parameters:
        fh_read - file to read (file - open for reading)
        fh_write - file to write (file - open for writing)
    Returns:
        None
    -------------------------------------------------------
    """

    i = 0
    line = fh_read.readline()
    while line != '':
        fh_write.write(f"[{i}] {line}")
        i += 1
        line = fh_read.readline()
    return


def student_stats(file_handle):
    """
    -------------------------------------------------------
    Get information from a file of file_handle and grades.
    Use: l_id, h_id, avg = student_stats(file_handle)
    -------------------------------------------------------
    Parameters:
        file_handle - student information file in the format
            surname,forename,id,mark (file - open for reading)
    Returns:
        l_id - the id of the student with the lowest mark (str)
        h_id - the id of the student with the highest mark (str)
        avg - the average mark (float)
    -------------------------------------------------------
    """
    highest_number = file_handle.readline()
    lowest_number = highest_number

    for line in file_handle:
        if line.split(',')[3] > highest_number.split(',')[3]:
            highest_number = line
        elif line.split(',')[3] < lowest_number.split(',')[3]:
            lowest_number = line

    avg = 0
    count = 0
    file_handle.seek(0)
    for line in file_handle:
        avg += int(line.split(',')[3])
        count += 1
    avg = avg / count
    return lowest_number.split(',')[2], highest_number.split(',')[2], avg
