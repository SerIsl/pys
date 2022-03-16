from funcs import *
  
while True:
    print("Çıkmak için q'ya basın.")
    barkod = input("Barkod numarasını girin:")
    
    if barkod.lower()  == "q":
        break

    isEmrim = isEmri(input("İş emri numarasını girin:"))
    
    if isEmrim.lower() == 'q':
        break
    
    hafta = input("Haftayı girin:")
    
    if hafta.lower() == 'q':
        break
    
    adet = input("Adet girin:")
    
    if adet.lower() == 'q':
        break
  
        
    seriNum(barkod, isEmrim, hafta, adet)