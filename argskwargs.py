# def sum(*numbers):
#     result = 0

#     for num in numbers:
#         if type(num) == int:
#             result += num
#     return result

# def message(*numbers):
#     result_string = ""
#     if numbers:
#         for number in numbers[:-1]:
#             if type(number) == int:
#                 if result_string != "":
#                     result_string += 'artı '
#                 result_string += f"{number} "
#         result_string += f"eşittir {numbers[-1]}"
#     return result_string

# my_list = [12, 13, 14, "serkan", False, 15, 25, 36, 47, 98]

# print(message(*my_list, sum(*my_list)))

# # print(sum(a, b, c, 40))

# def higher(**cars):
#     result_dict = {}
#     if cars:
#         for car_name, car_price in cars.items():
#             if car_price > 10000:
#                 result_dict[car_name] = car_price
#     return result_dict

# my_dick = {
#     "Araba1": 8500,
#     "Araba2": 9000,
#     "Araba3": 12000,
#     "Araba4": 8800,
#     "Araba5": 19000
# }

# print(higher(**my_dick))    

# def func(par1, par2, *args, **kwargs):
#     print(par1, par2)

#     if args:
#         print(args)
#     if kwargs:
#         for key, val, in kwargs.items():
#             print(key, val)


# func(1, 2)
# func(1, 2, 3, 4)
# func(1, 2, 3, 4, end=3, sep=4 )

# my_list = [3, 5, 7, 9, 12, 2, 5, 7, 44]

# def fact(a):
#     res = 1
    
#     while a > 0:
#         res *= a
#         a -= 1

#     return res

# def pr(*args):
#     resu = 0

#     for nu in args:
#         resu += fact(nu)/(nu+1)

#     return resu

# print(pr(*my_list))

# a = "2,5 kw\n2x1,70 kw\n0,90 kw"
# b = a.split(sep="\n")
# print(a)

# result = 0 

# for x in b:
#     x1 = x.split(" ")[0]
#     if "x" in x1:
#         carp = x1.split("x")
#         result += float(carp[0])*float(carp[1].replace(",", "."))
#     else:
#         result += float(x1.replace(",", "."))
        

# print(round(result, ndigits=3))

# Karekök hesap algoritması
sayi = 1
a = sayi
for i in range(sayi):
    a = (a + (sayi/a))*0.5
    print(a)
    t = a
    if t*t < t:
        break

print(a)
print(sayi**(1/2))  