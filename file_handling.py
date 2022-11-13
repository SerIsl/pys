from http.client import OK
from ean import *
from main import *

a = """Yapmak istediğiniz işlemi seçiniz:
            1: Ean kontrol
            2: Ean Oluşturmak
            3: Barkod Oluşturmak."""


while True:
    giris = input(a)

    if giris.lower() == "ok":
        break

    int_giris = int(giris)
    if int_giris == 1:
        ean_kontrol(giris)
    elif int_giris == 2:
        ean_olusturmak()
    elif int_giris == 3:
        seri_olusturmak()
    