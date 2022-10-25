from funcs import *
from seri_num import *
  
while True:

    print()
    print("Çıkmak için q'ya basın.")
    barkod = input("Barkod numarasını girin:")
    
    if barkod.lower()  == "q":
        break

    isEmrim = input("İş emri numarasını girin:")
    
    if isEmrim.lower() == 'q':
        break
    
    hafta = input("Haftayı girin:")
    
    if hafta.lower() == 'q':
        break
    
    adet = input("Adet girin:")
    
    if adet.lower() == 'q':
        break
  
        
    seri = SeriNum(barkod, isEmrim, hafta, adet)
    seri.printe()


