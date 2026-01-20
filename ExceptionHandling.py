# Functions
def sum_of_five_nums(a, b, c, d, e):
    return a+b+c+d+e


# Exception Handling
try:
    name = input('Enter your name: ')
    year_born = input('year you born: ')
    age = 2026 - int(year_born)
    print(f'You are {name}. And your age is {age}')
except:
    print(e)

# Unpacking

lst = [1, 2, 3, 4, 5]
# print(sum_of_five_nums(lst)) error cause the other four wasn't called
print(sum_of_five_nums(*lst))
