import numpy

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
my_dict = {
    'Malzeme Kodu': 'YP-01-015-001', 
    'Malzeme Tanımı': 'KAZAN CERCEVE DKP 60X90', 
    'Malzeme İng.Tanımı': 'X', 
    'Miktar': 300.0, 
    'Toplanan': 300.0, 
    'Kalan': 0.0, 
    'Sandık/Miktar': '44   /   43', 
    'Sandık/Miktar.1': '45   /   43', 
    'Sandık/Miktar.2': '46   /   43', 
    'Sandık/Miktar.3': '47   /   43', 
    'Sandık/Miktar.4': '48   /   43', 
    'Sandık/Miktar.5': '49   /   43', 
    'Sandık/Miktar.6': '50   /   42',
    'Sandık/Miktar.7': nan, 
    'Sandık/Miktar.8': nan, 
    'Sandık/Miktar.9': nan
    }
def cells(satir):
    malzeme_kodu = ""
    mydict1 = []

    for key, value in satir.items():
        kasa_no = 0
        adet = 0
        tempdict = {}
        if type(value) != str:
            continue 

        if key == "Malzeme Kodu":
            malzeme_kodu = value
        elif "Sandık/Miktar" in key:
            
            kasa_no = "M"+value.split("/")[0].replace(" ", "")
            adet = value.split("/")[1].replace(" ", "")
            tempdict["Kasa No"] = kasa_no
            tempdict["malzeme_kodu"] = malzeme_kodu
            tempdict["adet"] = adet
            mydict1.append(tempdict)
    
    print(*mydict1, sep="\n")


cells(my_dict)