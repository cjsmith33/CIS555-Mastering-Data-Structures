"""
Functions demonstrating using other functions as parameters.

These two functions are implementations of the famous fold functions.  A variation of
fold is called "reduce", which is part of Google's famous map-reduce set-up.

Author: Charles Smith
Date: 13 January 2021
"""


def fold_left(f,seq,value):
    """
    Returns the result of folding f left over seq, starting with value.

    To fold a function f from the left, we
    * Start with value in the accumulator
    * Iterate over the sequence normally
    * At each step, apply f to the accumulator and the next element
    * After applying f, make the new value the accumulator

    Example: Suppose f is - (subtraction), seq is (1,2,3,4) and value is 0.  Then
    the result is

        ((((0-1)-2)-3)-4) = -10

    Parameter f: the function to fold
    Precondition: f is a function that takes two arguments of the same time, and
    returning a value of the same type

    Parameter seq: the sequence to fold
    Precondition: seq is a sequence (tuple, string, etc.) whose elements are the
    same type as that returned by f

    Parameter value: the initial starting value
    Precondition: value has the same type as the return type of f
    """
    # original code failed: The call fold_left(duplicate, 'hello', 'ol')
    # returns 'ooll', not 'oollll'.
    #result = value
    #if type(value) == int:
        #accum = 0
        #for item in seq:
            #accum = accum + f(value,item)
            #result = accum
    #else:
        #accum = (value)
        #result = f(accum,seq)
        #return result

    accum = (value)
    #print(type(value))
    #print(type(f))
    for item in seq:
        accum = f(accum, item)
    return accum



def fold_right(f,seq,value):
    """
    Returns the result of folding f right over seq, starting with value.

    To fold a function f from the right, we
    * Start with value in the accumulator
    * Iterate over the sequence right-to-left
    * At each step, apply f to the next element and the accumulator
    * After applying f, make the new value the accumulator

    Example: Suppose f is - (subtraction), seq is (1,2,3,4) and value is 0.  Then
    the result is

        (1-(2-(3-(4-0)))) = -2

    Parameter f: the function to fold
    Precondition: f is a function that takes two arguments of the same time, and
    returning a value of the same type

    Parameter seq: the sequence to fold
    Precondition: seq is a sequence (tuple, string, etc.) whose elements are the
    same type as that returned by f

    Parameter value: the initial starting value
    Precondition: value has the same type as the return type of f
    """
    accum = (value)
    #print(type(value))
    #print(type(f))
    rev = ()

    #Question: what is the best way to reverse a string
    if len(seq) > 1:
        x=1
        for item in seq:
            rev = rev + (seq[len(seq) - x], )
            x=x+1
            #print(seq)
        seq = rev

    for item in seq:
        #print(item)
        accum = f(item, accum)
    return accum

    #Using a built in function 'reversed'
    #################################
    #for item in reversed(seq):
        #print(item)
        #accum = f(item, accum)
    #return accum
