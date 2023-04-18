from funcs import *
from seri_num import *

def seri_olusturmak():
    while True:

        print()
        print("Çıkmak için q'ya, baştan başlamak için v'ye basın.")
        barkod = input("Barkod numarasını girin:")
        
        if barkod.lower()  == "q":
            break
        elif barkod.lower()  == "v":
            continue

        isEmrim = input("İş emri numarasını girin:")
        
        if isEmrim.lower() == 'q':
            break
        elif isEmrim.lower() == 'v':
            continue
        
        hafta = input("Haftayı girin:")
        
        if hafta.lower() == 'q':
            break
        elif hafta.lower() == 'v':
            continue
        
        adet = input("Adet girin:")
        
        if adet.lower() == 'q':
            break
        elif adet.lower() == 'v':
            continue
    
            
        seri = SeriNum(barkod, isEmrim, hafta, adet)
        seri.printe()


