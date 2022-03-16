# def deneme():
#     print('abc0')

# f = deneme
# f()
# deneme()

# def deneme():
#     print('deneme fonksiyonu çalışıyor.')

#     def test():
#         return 'test fonksiyonu çalışıyor'  
#     return test

# deneme()

# def deneme():
#     return 'deneme fonksiyonu çalışıyor'

# def ikinci(f):
#     print('ikinci fonksiyon çalışıyor')

#     print(f())

# def deco(msg1, msg2):
#     def arakatman(f):
#         def wrapper(*args):
#             print(msg1)

#             f(*args)

#             print(msg2)

#         return wrapper
#     return arakatman        

# # @deco
# # def yazdir():
# #     print('yazdir')


# # yazdir = deco(yazdir)

# # yazdir()

# @deco("Serkan", "İşler")
# def toplama(a, b):
#     print(a + b)

# toplama(3, 5)  

import time


def sure_olc(f):
    def wrapper(*args):
        baslangic = time.time()
        print(f"Başlangıç Zamanı: {baslangic}")

        f(*args)

        bitis = time.time()
        print(f"Bitiş Zamanı: {bitis}") 

        print(f"Geçen Zaman: {bitis - baslangic}")
    return wrapper
@sure_olc
def faktor(sayi):
    toplam = 1

    while sayi > 1:
        toplam = toplam * sayi
        sayi -= 1

    print(toplam)

faktor(500000)
