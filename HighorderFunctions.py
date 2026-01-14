# Functions
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
