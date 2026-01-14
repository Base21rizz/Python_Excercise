# Functions
def sum_numbers(nums):
    return sum(nums)


def sum_using_HOF(f, lst):
    summation = f(lst)
    return summation


def Function_as_return_value(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute


# Main Part
""" result1 = sum_numbers(1, 2, 3, 4, 5) = 15
    print(result1)
    This is wrong it is here just to understand """
