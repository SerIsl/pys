# import pickle

# with open("cities.bin", "rb") as dosya:
#   cities =  pickle.load(dosya)
#   print(cities)
from seri_num import SeriNum as SN
from main import *
from ean import *


a = """Yapmak isterdiğniz İşlemi Seçiniz:\n
        Barkod oluşturmak için: 1\n
        EAN oluşturmak için: 2\n
        Sıralama yapmak için: 3\n
        çıkmak için: ok\n
        yazınız."""
secim = input(a)

while True:
  secim = input(a)
  if a.lower() == "ok":
    break
  elif a == "1":
    seri_olusturmak()
  elif a == "2":
    ean_olusturmak()
  elif a == "3":
    pass

