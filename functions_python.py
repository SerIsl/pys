


# def generate_full_name():
#     first_name = "Serkan"
#     space = " "
#     last_name = "İşler"

#     full_name = first_name + space + last_name
#     return full_name

# print(generate_full_name())

# def add_two_numbers():
#     first_number = 2
#     second_number = 3

#     total = first_number + second_number
#     print(total)

# add_two_numbers()

# def greeting(name):
#     massage = name +" welcome to python for Everyone."
#     return massage

# print(greeting("Serkan"))

# def add_ten(num):
#     ten = 10
#     return num + ten

# print(add_ten(8))

# def square(num):
#     return num*num

# print(square(20))

# def area_of_circle(r):
#     PI = 3.14
#     area = PI*r**2
#     return area

# print(area_of_circle(10))

# def sum_of_nums(num):
#     total = 0
#     for i in range(num+1):
#         total += i
#     print(total)

# sum_of_nums(10000001)

# def sum_all_nums(*args):
#     total = 0
#     for i in args:
#         total += i

#     return total

# print(sum_all_nums(1, 2, 30, 65))

# def  square_n(a):
#     return a*a

# def do_sth(f, x):
#     return f(x)

# print(do_sth(square_n, 5))



# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

# def sum(num1, num2):
#     return num1+num2

# print(sum(5, 7))    

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

# def area_of_circle(r):
#     PI = 3.14
#     return PI * r * r

# print(area_of_circle(17))

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.




# def add_all_nums(*args):
#     nums = []
#     count = 0
#     for i in args:
#         if type(i) == str:
#             print("Numerik olmayanlar eklenmedi")
#             count += 1
#             continue
#         nums.append(i)

#     print(f"{count} tane eklenemedi.") if count > 0 else print(sep="")
#     print(f"{len(nums)} tane sayı eklendi.")
#     return sum(nums)

# print(add_all_nums(3, 4, "serkan", 11, 15, "şsldk"))

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 
# 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

# def convert_cel_to_fahr(cel):
#     return (cel*9/5)+32

# print(convert_cel_to_fahr(100))

# Write a function called check-season, it takes a month parameter and returns the 
# season: Autumn, Winter, Spring or Summer.

# def season(month):
#     aut = ['eylül', "ekim", "kasım"]
#     win = ['aralık', "ocak", "şubat"]
#     spr = ["mart", "nisan", "mayıs"]
#     # summ = ["haziran", "temmuz", "ağustos"]

#     if month in aut:
#         return "Autumn"
#     elif month in win:
#         return "Winter"
#     elif month in spr:
#         return "Spring"
#     else:
#         return "Summer"

# print(season("aralık"))
# Write a function called calculate_slope which return the slope of a linear equation
# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
# Declare a function named print_list. It takes a list as a parameter and it prints 
# out each element of the list.

# def print_list(lst):
#     for i in lst:
#         print(i)

lst = ["serkan", "işler", 4, 5]
# print_list(lst)

# Declare a function named reverse_list. It takes an array as a parameter and it 
# returns the reverse of the array (use loops).

# # def reverse_list(lst):
# #     reversed_l = []
# #     for i in range(len(lst)):
# #         tmp = lst.pop()
# #         reversed_l.append(tmp)
# #     return reversed_l


# print(reverse_list(lst))        

# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]
# Declare a function named capitalize_list_items. It takes a list as a parameter 
# and it returns a capitalized list of items

# def capitalize_list_item(lst):
#     capitalized_list = []
#     for i in lst:
#         if type(i) != str:
#             capitalized_list.append(i)
#             continue
#         capitalized_list.append(i.capitalize())
#     return capitalized_list

# print(capitalize_list_item(lst))

# Declare a function named add_item. It takes a list and an item parameters. 
# It returns a list with the item added at the end.

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9]
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]

# def add_item(lst, item):
#     list_c = lst.copy()
#     list_c.append(item)
#     print(lst)
#     return list_c
# print(add_item(food_staff, "Serkan"))
# print(add_item(numbers, 5))

# Declare a function named remove_item. It takes a list and an item parameters. 
# It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))  # [2, 7, 9]

# def remove_item(lst, item):
#     removed_list = lst.copy()
#     removed_list.remove(item)
#     return removed_list

# print(remove_item(food_staff, "Mango"))
# Declare a function named sum_of_numbers. It takes a number parameter and 
# it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10)) # 55
# print(sum_all_numbers(100)) # 5050

# def sum_of_numbers(num):
#     total = 0
#     for i in range(num+1):
#         total += i

#     return total

# print(sum_of_numbers(10))

# Declare a function named sum_of_odds. It takes a number parameter and it adds 
# all the odd numbers in that range.
# def sum_of_odd(num):
#     total = 0
#     for i in range(num+1):
#         if i%2 != 0:
#             total += i
#     return total

# print(sum_of_odd(50))



# Declare a function named sum_of_even. It takes a number parameter and it adds 
# all the even numbers in that - range.
# Exercises: Level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter
#  and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.

# def evens_and_odds(num):

#     even = 0
#     odd = 0
#     for i in range(num+1):
#         if i%2 == 0:
#             even += 1
#         else:
#             odd += 1
#     print("The number of odds are ", odd)
#     print("The number of evens are ", even)

# evens_and_odds(757)


# Call your function factorial, it takes a whole number as a parameter and
#  it return a factorial of the number
# def fact(num):
#     fact = 1
#     for i in range(1, num+1):
#         fact *= i

#     print(fact)

# fact(6)
# Call your function is_empty, it takes a parameter and it checks 
# if it is empty or not
# Write different functions which take lists. They should calculate_mean, 
# calculate_median, calculate_mode, calculate_range, calculate_variance, 
# calculate_std (standard deviation).
# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.

# def is_prime(num):
#     count = 0
#     bolen = []
#     for i in range(1, num+1):
#         if num % i == 0:
#             count += 1
#             bolen.append(i)
#     if count == 2:
#         print("Sayı asal.")
#         print(bolen)
#     else:
#         print("Sayı asal değil :(") 
#         print(bolen)
#         print(len(bolen))

# is_prime(61)

# Write a functions which checks if all items are unique in the list.

# def is_unique(lst):
    # find = []
    # for i in lst:
    #     for j in lst:
    #         if j == i:
    #             find.append(i)
    #     if len(find) > 1:
    #         # print("unique değil")
    #         return False
    #     else:
    #         find.clear()
    # else:
    #     # print("unique ")
    #     return True


# is_unique([1, 2, 3, 4, 1, 65, 48, 7])



# Write a function which checks if all the items of the list are of the same data type.
# Write a function which check if provided variable is a valid python variable
# Go to the data folder and access the countries-data.py file.
# Create a function called the most_spoken_languages in the world. 
# It should return 10 or 20 most spoken languages in the world in descending order
# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.


# from random import randint as ra

# def suffle_list(x):
#     suffled_list = []
#     num = []
#     count = 0
#     while True:
#         num = [ra(0, len(x)-1) for i in range(len(x))]
#         if is_unique(num):
#             break

#     for i in num:
#         suffled_list.append(x[i])

#     return suffled_list

# a = [1, 2, 3, 4, 53, 68, 75]
# b = ["elma", "armut", "muz", "portakal", "ejder meyvesi", "mandalina", "ayva"]
# print(suffle_list(b), suffle_list(a), sep="\n") 

# language = "Python"
# lst = [i for i in language]
# print(lst)

# numbers = [i for i in range(11)]
# squares = [i * i for i in range(11)]
# numb = [(i, i * i) for i in range(11)]
# print(numbers)
# print(squares)
# print(numb)


# numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]

# even_numbers = [i for i in range(21) if i % 2 == 0]
# odd_numbers = [i for i in range(21) if i % 2 != 0]
# pos_even_num = [i for i in numbers if i > 0 and i % 2 == 0]
# print(even_numbers)
# print(odd_numbers)
# print(pos_even_num)

# list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flat_lst = [num for row in list_of_lists for num in row]

# print(flat_lst)

# x = lambda par1, par2, par3: par1 + par2 + par3

# print(x(1, 2, 3))

# print((lambda a, b: a+b)(2, 3))

# square = lambda x: x ** 2
# # print(square(6))
# cube = lambda y: y ** 3
# print(cube(8))

# multiple_veriable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
# print(multiple_veriable(5, 5, 3))

# def power(x):
#     return lambda n: x ** n

# cube = power(3)(3)
# print(cube)

# two_power_of_five = power(2)(5)
# print(two_power_of_five)

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

# nums = [i for i in numbers if i <= 0]
# print(nums)
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

# num_lst = [i for num1 in list_of_lists for num2 in num1 for i in num2]
# print(num_lst)

# nums = [(i, i**0, i**1, i**2, i**3, i**4, i**5) for i in range(11)]

# print(*nums, sep="\n")

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

country = [[i.upper(), i.upper()[:3], k.upper()] for co in countries for i, k in co]
# print(country)
country_dict = [{"country": i.upper(), "city": k.upper()} for co in countries for i, k in co]
# print(country_dict)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
names_lst = [i + " " + k for nm in names for i, k in nm]
# print(names_lst)

solve = lambda a, b, c: a ** 2 + 2 * b - 2+c

print(solve(1, 2, 3))