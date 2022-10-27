
import numpy
import pandas as pd

# class Coordinate:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y

#     def __repr__(self) -> str:
#         return "Coord: " + str(self.__dict__)

# def add(a, b):
#     return Coordinate(a.x + b.x, a.y + b.y)

# def sub(a, b):
#     return Coordinate(a.x - b.x, a.y - b.y) 
# one = Coordinate(100, 200)
# two = Coordinate(300, 200)
# three = Coordinate(-100, -100)


# def wrapper(func):
#     def checker(a, b):
#         if a.x < 0 or a.y < 0:
#             a = Coordinate(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)
        
#         if b.x < 0 or b.y < 0:
#             b = Coordinate(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)
        
#         ret = func(a, b)
#         if ret.x < 0 or ret.y < 0:
#             ret = Coordinate(ret.x if ret.x > 0 else 0, ret.y if ret.y > 0 else 0)
#         return ret
#     return checker

# add = wrapper(add)
# sub = wrapper(sub)

# print(sub(one, two))
# print(add(one, three))

dosya = "PR-220919-AG PROLUX 1200 TK BL 19.10.2022.XLSX"

df = pd.read_excel(dosya, dtype=str)


sozluk = df.to_dict("records")

# print(sozluk)


# my_dict = {
#     'Malzeme Kodu': 'YP-01-015-001', 
#     'Malzeme Tanımı': 'KAZAN CERCEVE DKP 60X90', 
#     'Malzeme İng.Tanımı': 'X', 
#     'Miktar': 300.0, 
#     'ToplaNone': 300.0, 
#     'Kalan': 0.0, 
#     'Sandık/Miktar': '44   /   43', 
#     'Sandık/Miktar.1': '45   /   43', 
#     'Sandık/Miktar.2': '46   /   43', 
#     'Sandık/Miktar.3': '47   /   43', 
#     'Sandık/Miktar.4': '48   /   43', 
#     'Sandık/Miktar.5': '49   /   43', 
#     'Sandık/Miktar.6': '50   /   42',
#     'Sandık/Miktar.7': None, 
#     'Sandık/Miktar.8': None, 
#     'Sandık/Miktar.9': None
#     }
lisem = {
            'CODE/KOD': '10-18-170-001', 
            'DESCRIPTION (TR)': 'PUL CANAK M3', 
            'DESCRIPTION (ENG)': 'STAMP CIRCLE M3', 
            'BİRİM / UNIT': 'pcs', 
            'MKT/QTY': 5400, 
            'SANDIK=1    KOLİ=2': None, 
            'SANDIK NO / BOX NUM.': 30, 
            'SANDIK İÇ ADETİ / QTY. IN THE BOX': 5400, 
            'SANDIK NO / BOX NUM..1': 20, 
            'SANDIK İÇ ADETİ / QTY. IN THE BOX.1': 500, 
            'SANDIK NO / BOX NUM..2': "B1", 
            'SANDIK İÇ ADETİ / QTY. IN THE BOX.2': 50, 
            'SANDIK NO / BOX NUM..3': None, 
            'SANDIK İÇ ADETİ / QTY. IN THE BOX.3': None, 
            'SANDIK NO / BOX NUM..4': None, 
            'SANDIK İÇ ADETİ / QTY. IN THE BOX.4': None, 
            'SANDIK NO / BOX NUM..5': None, 
            'SANDIK İÇ ADETİ / QTY. IN THE BOX.5': None, 
            'SANDIK NO / BOX NUM..6': None, 
            'SANDIK İÇ ADETİ / QTY. IN THE BOX.6': None, 
            'SANDIK NO / BOX NUM..7': None, 
            'SANDIK İÇ ADETİ / QTY. IN THE BOX.7': None, 
            'SANDIK NO / BOX NUM..8': None, 
            'SANDIK İÇ ADETİ / QTY. IN THE BOX.8': None, 
            'SANDIK NO / BOX NUM..9': None, 
            'SANDIK İÇ ADETİ / QTY. IN THE BOX.9': None, 
            'Unnamed: 26': None, 
            'Unnamed: 27': None, 
            'Unnamed: 28': None, 
            'Unnamed: 29': None, 
            'Qty (LOADED)': 5400, 
            'Missing/Exceed': 0
        }

def cells(satir):
    malzeme_kodu = ""
    mydict1 = []
    tmp = []

    for key, value in satir.items():
    
        tempdict = {}
        if value == None:
            continue 

        if "CODE" in key:
            malzeme_kodu = value
        elif "SANDIK NO" in key:
            if type(value) == int:
                tmp.append('M'+str(value))
            else:
                tmp.append(value)
            
        elif "ADET" in key:
            tempdict["Kasa No"] = tmp.pop()
            tempdict["Malzeme Kodu"] = malzeme_kodu
            tempdict["Adet"] = value
            mydict1.append(tempdict)
    
    print(*mydict1, sep="\n")

cells(lisem)

a = None
print(type(a))




# a = lambda x: list(x.items())
# print(a(lisem))