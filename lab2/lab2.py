#
# Author: angel suleiman
# Student Number:152961231
#
# Place the code for your lab 2 here.  Read the specs carefully.  
#
# To test, run the following command :
#     python test_lab2.py
#

# Write the following 3 functions recursively

def factorial(number):
    # base case
    if number == 0 or number == 1:
        return 1
    # recursive case
    result = number * factorial(number - 1)
    return result

def linear_search(values, key, pos=0):
    # stop if we've checked the whole list
    if pos >= len(values):
        return -1
    # found the key
    if values[pos] == key:
        return pos
    # keep searching
    return linear_search(values, key, pos + 1)


def binary_search(values, key, start=0, end=None):
    if end is None:
        end = len(values) - 1
    if start > end:
        return -1

    middle = (start + end) // 2

    if values[middle] == key:
        return middle
    elif key < values[middle]:
        return binary_search(values, key, start, middle - 1)
    else:
        return binary_search(values, key, middle + 1, end)
