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


# Excercise
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = [i for i in numbers if i <= 0]
print(filtered)

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
output = [item for sublist in list_of_lists for inner in sublist for item in inner]
print(output)

Pattern = [tuple([n] + [n**i for i in range(6)]) for n in range(11)]
print(Pattern)

countries = [[('Finland', 'Helsinki')], [
    ('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
output = [[c.upper(), c[:3].upper(), cap.upper()]
          for sub in countries for c, cap in sub]
print(output)

output = [{'Country': val1.upper(), 'City': val2.upper()}
          for sub in countries for val1, val2 in sub]
print(output)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')],
         [('Donald', 'Trump')], [('Bill', 'Gates')]]
output = [name + ' ' + surname
          for sub in names for name, surname in sub]
print(output)
