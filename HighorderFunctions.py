# Functions
from functools import reduce


def sum_numbers(nums):
    return sum(nums)


def sum_using_HOF(f, lst):
    summation = f(lst)
    return summation


def square(x):
    return x**2


def cube(x):
    return x**3


def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)


def Function_as_return_value(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute


def add_ten():
    ten = 10

    def add(num):
        return num + ten
    return add

# Without Decorator


def greeting():
    return 'Welcome to python'


# we will use this as the first decorator for the multiple decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
# Without Decorator


# With Decorator
'''This decorator function is a higher order function that takes a function as a parameter'''


def uppercase_decorator_WD(function):
    def wrapper_WD():
        func_WD = function()
        make_uppercase_WD = func_WD.upper()
        return make_uppercase_WD
    return wrapper_WD


@uppercase_decorator_WD
def greeting_WD():
    return 'Welcome to Python'
# Applying Multiple Decorators to a Single Function
# Second decorator


def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper


@split_string_decorator
@uppercase_decorator
def greeting_WMD():
    return 'Welcome to Python'

# Accepting Parameters in Decorator Functions


def decorator_with_parameters(function):
    def wrapper_accepting_parameters(par1, par2, par3):
        function(par1, par2, par3)
        print("I live in {}".format(par3))
    return wrapper_accepting_parameters


@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(first_name, last_name))


# Built-in Higher Order Functions (Map)
# Syntax map(function, iterable)
numbers = [1, 2, 3, 4, 5]


def square(x):
    return x**2


# Built-in Higher Order Functions (Filter)
# Syntax map(function, iterable)
numbers = [1, 2, 3, 4, 5]


def is_even(num):
    if num % 2 == 0:
        return True
    return False


# Built-in Higher Order Functions (Reduce)
# Syntax map(function, iterable)
numbers_str = ['1', '2', '3', '4', '5']


def add_two_nums(x, y):
    return int(x) + int(y)


# Main Part


""" result1 = sum_numbers(1, 2, 3, 4, 5) = 15
    print(result1)
    This is wrong it is here just to understand """

result2 = sum_using_HOF(sum_numbers, [1, 2, 3, 4, 5])
print(result2)

result_FARV = Function_as_return_value('square')
print(result_FARV(3))
result_FARV = Function_as_return_value('cube')
print(result_FARV(3))
result_FARV = Function_as_return_value('absolute')
print(result_FARV(-3))

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20

# Without Decorator
g = uppercase_decorator(greeting)
print(g())
# Without Decorator
# With Decorator
print(greeting_WD())
# With Decorator

# Applying Multiple Decorators to a Single Function
print(greeting_WMD())

# Accepting Parameters in Decorator Functions
print_full_name("Shoumik", "Islam", "Finland")

# Built-in Higher Order Functions (Map)
numbers_squared = map(square, numbers)
print(list(numbers_squared))
# using lambda
numbers_squared_lambda = map(lambda x: x ** 2, numbers)
print(list(numbers_squared_lambda))

# Built-in Higher Order Functions (Filter)
even_numbers = filter(is_even, numbers)
print(list(even_numbers))

# Built-in Higher Order Functions (Reduce)
total = reduce(add_two_nums, numbers_str)
print(total)
