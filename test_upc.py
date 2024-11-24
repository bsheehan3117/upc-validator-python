'''
    CS5001
    Spring 2023
    HW4

    Brendan Sheehan

    This program tests the is_valid_upc function
'''

from upc import is_valid_upc

def test_is_valid_upc(list_of_integers, expected):

    '''Function tst_is_valid_upc

    Parameters:
    A list of integers representing a UPC code
    excpected output
    return: nothing, print input and actual vs expected

    Examples:
    is_valid_upc([0,7,3,8,5,4,0,0,8,0,8,9]): True
    is_valid_upc([9, 6, 3, 2, 2, 2, 8, 0, 8]): True
    is_valid_upc([0,0,0,0,0,0]): False
    is_valid_upc([100]): False
    is_valid_upc([9, 6, 3, 2, 2, 0 ,3, 6, 9]): False
    is_valid_upc([2, 4, 9, 1, 2, 1, 3, 5, 5, 8]): False
    '''
    actual = is_valid_upc(list_of_integers)
    print("t\Expected = ", expected)
    print("t\Result = ", actual)

def main():

    # test 1 even num of digits sum to multiple of 10 
    test_is_valid_upc([0,7,3,8,5,4,0,0,8,0,8,9], True)
    [9,8,0,8,0,0,4,5,8,3,7,0]
    
    # test 2 odd num of digits sum to multiple of 10
    test_is_valid_upc([9, 6, 3, 2, 2, 2, 8, 0, 8], True)

    # test 3 digits sum to 0
    test_is_valid_upc([0,0,0,0,0,0], False)

    # test 4 list lest than 2 digits
    test_is_valid_upc([100], False)

    # test 5 odd num of digits dont sum to mult of 10
    test_is_valid_upc([9, 6, 3, 2, 2, 0 ,3, 6, 9], False)

    # test 6 even num of digits dont sum to mult of 10
    test_is_valid_upc([2, 4, 9, 1, 2, 1, 3, 5, 5, 8], False)

if __name__ == "__main__":
    main()   
