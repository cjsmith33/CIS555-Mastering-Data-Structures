"""
Module to show off tuple methods.

Neither this module nor the function should import the introcs module.  In addition,
the function should not use a loop or recursion.

Author: Charles Smith
Date: 10 January 2021
"""


def replace_first(tup,a,b):
    """
    Returns a copy of tup with the first value of a replaced by b

    Examples:
        replace_first((1,2,1),1,3) returns (3,2,1)
        replace_first((1,2,1),4,3) returns (1,2,1)

    Parameter tup: The tuple to copy
    Precondition: tup is a tuple of integers

    Parameter a: The value to replace
    Precondition: a is an int

    Parameter b: The value to replace with
    Precondition: b is an int
    """
    newTup = ()
    result = tup
    if tup.count(a) > 0:
        replace = tup.index(a)
        newTup = tup[:replace] + (b,) + tup[replace + 1:len(tup)]
        result = newTup

    return result
