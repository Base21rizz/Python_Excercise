language = 'pyhton'
lst = [i for i in language]
print(type(lst))
print(lst)

# generate number from 1-19
number = [i for i in range(19)]
print(number)

# generating squares in range using list comprehension 1^2-10^2
squares = [i*i for i in range(11)]
print(squares)

# Making list of tuples using using list comprehension
numbers = [(i, i * i) for i in range(11)]
print(numbers)

# Generating even numbers using list
even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)

# Generating odd numbers using list
odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)

# Filtering
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)
negative_numbers = [i for i in numbers if i < 0]
print(negative_numbers)

""" Lambda function
         syntax
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3)) """

# function


def add_two_num(a, b):
    return a+b


def power(x):
    return lambda n: x**n
# add_two_numbers = lambda a,b: a+b (commented out because pep8 makes it normal function)


print(add_two_num(2, 3))
# print(add_two_numbers(2,3)) (commented out because pep8 makes it normal function)
print((lambda a, b: a+b)(2, 3))  # self invoking lambda function
cube = power(2)(3)
print(cube)
two_power_of_five = power(2)(5)
print(two_power_of_five)
