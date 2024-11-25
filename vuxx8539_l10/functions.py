"""
-------------------------------------------------------
CP104 Lab 10: Files
-------------------------------------------------------
Author:  Jeff Vu
ID:      169058539
Email:   vuxx8539@mylaurier.ca
__updated__ = "0000-00-00"
-------------------------------------------------------
"""
ID_FLD = 0  
FN_FLD = 1  
LN_FLD = 2 
BL_FLD = 3  
DT_FLD = 4 


def customer_record(fv, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fv, n)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
        n - the number of the record to return (int < 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    # Initialize the final result if record n is not found.
    result = []
    # Initialize the record counter.
    i = 0
    # Perform the priming file read.
    line = fv.readline()

    while line != "" and i < n:
        # Check for end of file and record count.
        i += 1
        line = fv.readline()

    if line != "":
        # Record n was found.
        result = line.strip().split(",")
    return result


def customer_by_id(fv, id_number):
    """
    -------------------------------------------------------
    Find the record for a given ID in a sequential file.
    Use: result = customer_by_id(fv, id_number)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
        id_number - the id_number to match (str)
    Returns:
        result - the record with id_number if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    # Initialize the final result if record n is not found.
    result = []
    # Perform the priming file read.
    line = fv.readline()

    while line != "" and result == []:
        # Check for end of file and and matching ID.
        fields = line.strip().split(",")

        if fields[ID_FLD] == id_number:
            # Matching ID found.
            result = fields
        else:
            # Read the next line only if ID not found.
            line = fv.readline()
    return result


def customer_best(fv):
    """
    -------------------------------------------------------
    Find the customer with the largest balance.
    Assumes file is not empty.
    Use: result = customer_best(fv)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
    Returns:
        result - the record with the greatest balance (list)
    -------------------------------------------------------
    """
    # Initialize a maximum balance.
    result = fv.readline().strip().split(",")
    # Get the next line.
    line = fv.readline()

    while line != "":
        fields = line.strip().split(",")

        if float(result[BL_FLD]) < float(fields[BL_FLD]):
            # Update the maximum balance to the larger balance.
            result = fields

        # Read the next line of the file.
        line = fv.readline()
    return result


def customer_best_2(fv):
    """
    -------------------------------------------------------
    Alternate version
    -------------------------------------------------------
    """
    # Initialize a maximum balance and final result.
    line = fv.readline()
    result = line.strip().split(",")
    max_balance = float(result[BL_FLD])

    for line in fv:
        fields = line.strip().split(",")
        balance = float(fields[BL_FLD])

        if max_balance < balance:
            # Update the maximum balance to the larger balance.
            max_balance = balance
            result = fields
    return result


def customer_first(fv):
    """
    -------------------------------------------------------
    Find the customer with the earliest sign-up date.
    Assumes file is not empty.
    Use: result = customer_first(fv)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
    Returns:
        result - the record with the earliest sign-in date (list)
    -------------------------------------------------------
    """
    # Get the first date from the first line of the file.
    line = fv.readline()
    result = line.strip().split(",")
    # Read the next line in the file.
    line = fv.readline()

    while line != "":
        fields = line.strip().split(",")

        if result[DT_FLD] > fields[DT_FLD]:
            # Update the first date to the earlier date.
            result = fields
        # Read the next line of the file.
        line = fv.readline()
    return result


def customer_first_2(fv):
    """
    -------------------------------------------------------
    Alternate version
    -------------------------------------------------------
    """
    # Get the first date from the first line of the file.
    line = fv.readline()
    result = line.strip().split(",")
    first_date = result[DT_FLD]

    for line in fv:
        fields = line.strip().split(",")
        date = fields[DT_FLD]

        if first_date > date:
            # Update the first date to the earlier date.
            first_date = date
            result = fields
    return result


def customer_append(fv, fields):
    """
    -------------------------------------------------------
    Appends a customer record to a comma-delimited sequential file.
    Use: customer_append(fv, fields)
    -------------------------------------------------------
    Parameters:
        fv - file to add to (file - open for appending)
        fields - a list of the field data to append to the file (list)
    Returns:
       None
    -------------------------------------------------------
    """
    record_string = "{},{},{},{},{}\n".format(
        fields[ID_FLD], fields[FN_FLD], fields[LN_FLD], fields[BL_FLD],
        fields[DT_FLD])
    fv.write(record_string)
    return


def customer_append_2(fv, fields):
    """
    -------------------------------------------------------
    ALTERNATE VERSION
    -------------------------------------------------------
    """
    n = len(fields)

    for i in range(n - 1):
        fv.write("{},".format(fields[i]))
    fv.write("{}\n".format(fields[n - 1]))
    return


def number_stats(fv):
    """
    -------------------------------------------------------
    Returns statistics on the numbers in a file.
    Assumes file is not empty.
    Use: smallest, largest, total, average = number_stats(fv)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
    Returns:
        smallest - smallest number (int)
        largest - largest number (int)
        total - sum of all the numbers in the file (int)
        average - average of all the numbers (float)
    ------------------------------------------------------
    """
    # Get the first line
    line = fv.readline()
    v = int(line.strip())
    n = 1
    smallest = v
    largest = v
    total = v
    # Get the second line
    line = fv.readline()

    while line != "":
        v = int(line.strip())
        n += 1

        if v < smallest:
            smallest = v
        elif v > largest:
            largest = v
        total += v
        line = fv.readline()

    average = total / n
    return smallest, largest, total, average


def append_max_num(fv):
    """
    -------------------------------------------------------
    Appends a number to the end of fv. The number appended
    is the maximum of all the numbers currently in the file.
    Assumes file is not empty.
    Use: num = append_max_num(fv)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    line = fv.readline()
    v = int(line.strip())
    m = v

    while line != "":
        v = int(line.strip())

        if v > m:
            m = v
        line = fv.readline()
    fv.write("{}\n".format(m))
    return m


def append_increment(fv):
    """
    -------------------------------------------------------
    Appends a number to the end of the fv. The number appended
    is the last number in the file plus 1.
    Assumes file is not empty.
    Use: num = append_increment(fv)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    line = fv.readline()

    while line != "":
        v = int(line.strip())
        line = fv.readline()
    v = v + 1
    fv.write("{}\n".format(v))
    return v


def count_frequency_value(fv, value):
    """
    -------------------------------------------------------
    Counts the number of appearances of value in fv.
    Use: count = count_frequency_value(fv, value)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
        value - the value to count (int)
    Returns:
        count - the number of appearance of value in fv (int)
    ------------------------------------------------------
    """
    count = 0

    for line in fv:
        if int(line) == value:
            count += 1
    return count


def count_frequency_word(fv, word):
    """
    -------------------------------------------------------
    Counts the number of appearances of word in fv.
    Case is significant - line in file must match word in case.
    Use: count = count_frequency_word(fv, word)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
        word - the word to search for it in fv (str)
    Returns:
        count - the number of appearance of word in fv (int)
    ------------------------------------------------------
    """
    count = 0

    for line in fv:
        if line.strip() == word:
            count += 1
    return count


def find_longest(fv):
    """
    -------------------------------------------------------
    Finds the last word with longest length in fv.
    Assumes file is not empty.
    Use: word = find_longest(fv)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
    Returns:
        word - the last word with the longest length in fv (str)
    ------------------------------------------------------
    """
    word = fv.readline().strip()
    size = len(word)

    for line in fv:
        w = line.strip()
        n = len(w)

        if n >= size:
            size = n
            word = w
    return word


def find_shortest(fv):
    """
    -------------------------------------------------------
    Finds the first word with shortest length in fv.
    Assumes file is not empty.
    Use: word = find_shortest(fv)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
    Returns:
        word - the first word with the shortest length in fv (str)
    ------------------------------------------------------
    """
    word = fv.readline().strip()
    size = len(word)

    for line in fv:
        w = line.strip()
        n = len(w)

        if n < size:
            size = n
            word = w
    return word


def file_copy(fv_1, fv_2):
    """
    -------------------------------------------------------
    Copies the contents of fv_1 to fv_2.
    Any contents of fv_2 are overwritten.
    Use: file_copy(fv_1, fv_2)
    -------------------------------------------------------
    Parameters:
        fv_1 - source file (file - open for reading)
        fv_2 - target file (file - open for writing)
    Returns:
        None
    ------------------------------------------------------
    """
    for line in fv_1:
        fv_2.write(line)
    return


def file_copy_n(fv_1, fv_2, n):
    """
    -------------------------------------------------------
    Copies n record(s) from fv_1 (starting from the beginning of the file) to fv_2
    Use: file_copy_n(fv1, fv2, n)
    -------------------------------------------------------
    Parameters:
        fv_1 - source file (file - open for reading)
        fv_2 - target file (file - open for writing)
        n - the number of lines to copy (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    line = fv_1.readline()
    i = 0

    while line != "" and i < n:
        fv_2.write(line)
        line = fv_1.readline()
        i += 1
    return


def delete_line(fv, n):
    """
    UNUSED
    -------------------------------------------------------
    Removes line number n from fv.
    Lines are numbered starting with 0.
    Use: delete_line(fv, n)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading/writing)
        n - the line number to be removed (int >= 0)
    Returns:
        removed - the contents of the line that was removed (str)
    ------------------------------------------------------
    """
    lines = fv.readlines()

    if n < len(lines):

        for i in range(0, len(lines)):
            if i == n:
                removed = lines[i]
            else:
                fv.write(lines[i])
        fv.truncate()
    else:
        removed = ""
    return removed
