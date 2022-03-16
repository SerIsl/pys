# from unittest import result


# def sum_number(nums):
#     return sum(nums)

# def high_order_function(f, lst):
#     summation = f(lst)
#     return summation

# resultt = high_order_function(sum_number, [1, 2, 3, 4, 5])
# print(resultt)

# def square(x):
#     return x ** 2

# def cube(x):
#     return x ** 3

# def absolute(x):
#     if x >= 0:
#         return x
#     else: 
#         return -(x)

# def high_order_func(type):
#     if type == "square":
#         return squareQ
#     elif type == "cube":
#         return cube
#     elif type == "absolute":
#         return absolute

# ress = high_order_func("absolute")
# print(ress(-5))

# import telnetlib


# def add_ten():
#     ten = 10
#     def add(x):
#         return x + ten
#     return add

# closure_result = add_ten()

# print(closure_result(2))
# print(closure_result(10))

# def split_string_decorator(function):
#     def wrapper():
#         func = function()
#         splitted_string = func.split()
#         return splitted_string
#     return wrapper

# def uppercase_decarator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return wrapper





# @split_string_decorator
# @uppercase_decarator
# def greeting():
#     return "Welcome Home!"
# # g = uppercase_decarator(greeting)

# print(greeting())

# def decorator_with_paramaters(function):
#     def wrapper_accepting_parameters(para1, para2, para3):
#         function(para1, para2, para3)
#         print("I live in {}".format(para3))
#     return wrapper_accepting_parameters

# @decorator_with_paramaters
# def print_full_name(first_name, last_name, country):
#     print("I am {} {}. I love learn.".format(first_name, last_name, country))

# print_full_name("Serkan", "İşler", "Türkiye")

# numbers = [1, 2, 3, 4, 5]

# def square(x):
#     return x ** 2

# # numbers_squared = map(square, numbers)
# # print(*numbers_squared)

# numbers_squared = map(lambda x: x ** 2, numbers)

# numbers_str = ['1', '2', '3', '4', '5']

# numbers_int = map(int, numbers_str)
# print(list(numbers_int))

# from functools import reduce


# names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham'] 

# def change_to_upper(name):
#     return name.upper()

# names_upper_cased = map(change_to_upper, names)
# print(list(names_upper_cased))

# numbers = [1, 2, 3, 4, 5]

# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False

# def is_odd(num):
#     if num % 2 != 0:
#         return True
#     return False

# def is_name_long(name):
#     if len(name) > 7:
#         return True
#     return False

# def add_two_nums(x, y):
#     return int(x) + int(y)

# even_num = filter(is_even, numbers)
# odd_num = filter(is_odd, numbers)
# long_names = filter(is_name_long, names)

# numbers_str = ['1', '2', '3', '4', '5', '6', '7']
# total = reduce(add_two_nums, numbers_str)

# print(list(even_num))
# print(list(odd_num))
# print(list(long_names))
# print(total)

from functools import reduce
from tkinter.tix import Tree


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', "Türkmenistan"]
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use for loop to print each country in the countries list.
# for i in countries:
#     print(i)


# Use for to print each name in the names list.
# Use for to print each number in the numbers list. 

# Exercises: Level 2
# Use map to create a new list by changing each country to uppercase in the countries
#  list
# def upperer(arg):
#     return arg.upper()
# uppered = 



# Use map to create a new list by changing each number to its square in the numbers 
# list
# def squarer(x):
#     return x**2

# squared = list(map(squarer, numbers))    
# print(squared)

# Use map to change each name to uppercase in the names list
# Use filter to filter out countries containing 'land'.
# def is_contain(x):
#     if 'land' in x:
#         return True
#     return False

# land_countries = list(filter(is_contain, countries))

# print(land_countries)



# Use filter to filter out countries having exactly six characters.

# def is_six_characters(x):
#     if len(x) == 6:
#         return True
#     return False

# sixes = list(filter(is_six_characters, countries))
# print(sixes)


# Use filter to filter out countries containing six letters and more in the country 
# list.

# def is_six_letter(x):
#     count = 0
#     a = "bcçdfghjklmnpqrsştvwxyz"
#     letters = a + a.upper()
#     for i in x:
#         if i in letters:
#             count += 1
#     if count > 6:
#         return True
#     return False

# six_letters = list(filter(is_six_letter, countries))
# print(six_letters)
# # Use filter to filter out countries starting with an 'E'
# def start_with_e(x):
#     if x[0] == "e" or x[0] == "E":
#         return True
#     return False

# print(list(filter(start_with_e, countries)))
# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))


# Declare a function called get_string_lists which takes a list as a parameter and 
# then returns a list containing only string items.
def is_string(x):
    if type(x) == str:
            return True
    
    return False

def get_string_lists(x):
    return list(filter(is_string, x))

lst = [1, 2, "erkan", "meyve", True, [2, 2, 2], 3.6]

# print(get_string_lists(lst))
from country_list import countries


def decorator(function):
    def wrapper(x):
        function(x)
        print("Listenin eleman sayısı: ", len(x))
    return wrapper

def print_with_for(x):
    for i in x:
        print(i)

deco_printer = decorator(print_with_for)

lstr = lambda arg1, arg2, arg3: list(arg1(arg2, arg3))




# Use reduce to sum all the numbers in the numbers list.
# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

# deco_printer(lstr(filter, lambda x: "ia" in x, countries))

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.



# def letter(x):
#     letter_dict = {}
#     lamb = lambda a: a[0]
#     let_lst = map(lamb, x)

#     for i in let_lst:
#         if i not in letter_dict:
#             letter_dict[i] = 1    
#         else:
#             letter_dict[i] += 1

#     return letter_dict

# print(letter(countries))

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.
# deco_printer(lstr(filter, lambda x: countries.index(x)< 10,countries ))

# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

# deco_printer(lstr(filter, lambda x:  len(countries)-11 < countries.index(x),countries ))

# Sort countries by name, by capital, by population
from countries_data import countries_data_lst as cdl
countries_name = map(lambda x: {list(x.items())[0][1]:list(x.items())[3][1] }, cdl)
print(*list(countries_name), sep="\n")
# Sort out the ten most spoken languages by location.
# Sort out the ten most populated countries.