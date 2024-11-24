'''
    CS5001
    Spring 2023
    HW4
    
    Brendan Sheehan

    This is a function to determine the validity of
    a UPC code.
'''

def is_valid_upc(list_of_integers):

    '''Function: is_valid_upc
    Determines the validity of a UPC code.
    Parameters: List of integers (possible UPC)
    Returns: Boolean True if UPC is valid
    or False if UPC is not valid

    A valid UPC is determined via the following algorithm:
    List proceeds right to left
    Digits in even positions, including zero: no change
    Digits in odd positions: *3
    Sum the results
    Check: If the barcode has a valid UPC number,
    this result is a multiple of 10.
    '''
    
    # special case, if input < 2 digits, UPC not valid
    if len(list_of_integers) < 2:
        return False

    # reverse argument passed through function
    reversed_list = list_of_integers[::-1]
    print(reversed_list)

    # determine if an index is odd,
    # multiply the values held at odd indexes by 3
    for i in range(len(reversed_list)):
        if i % 2 == 1:
            reversed_list[i] *= 3

    # adding the values held at all indexes of the list
    sum = 0
    for i in range(len(reversed_list)):
        sum += reversed_list[i]

    # special case, if all digits have value 0, UPC not valid
    if sum == 0:
        return False

    # return true if sum is multiple of 10
    if sum % 10 == 0:
        return True
    # return false if sum not multiple of 10
    if sum % 10 != 0:
        return False

    

    

    
