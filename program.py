
from ean import *
from main import *
from sirala import *

a = """Yapmak istediğiniz işlemi seçiniz:
            1: Ean kontrol
            2: Ean Oluşturmak
            3: Barkod Oluşturmak
            4: Siralama yapmak
            
            Giriş yapın: \t"""


while True:
    print("-"*60)
    giris = input(a)
    print("-"*60)
    if giris.lower() == "ok":
        break

    int_giris = int(giris)
    if int_giris == 1:
        ean_kontrol(giris)
    elif int_giris == 2:
        ean_olusturmak()
    elif int_giris == 3:
        seri_olusturmak()
    elif int_giris == 4:
        sirala()