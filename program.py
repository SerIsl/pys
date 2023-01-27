import os
import subprocess
from ean import *
from main import *
from sirala import *
from denee import *

def kasa():
    os.chdir("C:\\Users\\SERKAN\\Desktop\\gitproject\\MyWorkouts")
    subprocess.run(["python", "prep_casa.py"])

def program():
    a = """Yapmak istediğiniz işlemi seçiniz:
                1: Ean kontrol
                2: Ean Oluşturmak
                3: Barkod Oluşturmak
                4: Siralama yapmak
                5: Kasa
                ok: Çıkış yapmak
                
                Giriş yapın: \t"""

    b = ["1", "2", "3", "4", "5", "6", "ok"]
    while True:
        print("-"*60)
        giris = input(a)
        print("-"*60)
        if giris.lower() == "ok":
            break
        elif giris not in b:
            print("Lütfen yapmak istediğiniz işlemi yukarıdaki listeden seçin!")
            continue

        int_giris = int(giris)
        if int_giris == 1:
            ean_kontrol(giris)
        elif int_giris == 2:
            ean_olusturmak()
        elif int_giris == 3:
            seri_olusturmak()
        elif int_giris == 4:
            sirala()
        elif int_giris == 5:
            kasa()
        elif int_giris == 6:
            cozumle()

doldur = lambda x, y: print(f"{x}"*y)
degis = lambda x, y, z: print(x.replace(y, z)) 

if __name__ == "__main__":
    program()