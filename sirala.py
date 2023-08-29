import pandas as pd
import os
import re

def yol_rep(x):
    yolr = re.sub(r"\\", "\\\\", x)
    return yolr

def eklemeli(x):

    os.chdir(yol_rep(r"C:\Users\SERKAN\Desktop\yeni_klasor"))
    barkod = input("barkodu giriniz: ")
    
    li = [barkod + f"{str(y):>04}" for y in x]

    df = pd.DataFrame(li,columns=["Barkods"])
    df.to_csv("Barkods.csv", sep=";", index=False)
    print("Barkods.csv kullanıma hazır.")

def sirala():
    all = set()
    same = {}
    entry = ""
    to_csv = False
    mod = int(input("Lütfen Modu seçin (0/1):"))
    if mod == 0:
        secim = input("Csv çıktısı almak istiyor musunuz? E/H")
        if secim.lower() == "e":
            to_csv = True
    while True:
        print(f"\nGirilerin toplam sayısı: {len(all)}")
        entry = input('Bitirmek için ok yaz!\ngiriş yap:\t')

        

        if entry.lower() == "ok":
            break
        
        if mod == 1:
            if entry in all:
                print("Hey dostum bu daha önce girilmiş başka bi tane dene!")
                same[entry] = same.setdefault(entry, 0) + 1
                continue
            else:
                all.add(entry)
        else: 
            intent = int(entry)
            if intent in all:
                print("Hey dostum bu daha önce girilmiş başka bi tane dene!")
                same[entry] = same.setdefault(entry, 0) + 1
                continue
            else:
                all.add(intent)
    list_all = list(all)
    list_all.sort()
    print(*list_all, sep="\n")
    print("Toplam kayıt sayısı:", len(list_all))
    print("Benzerler: ", same)
    print("Benzerlerin toplam sayısı: ", sum(list(same.values())))

    if to_csv == True:
        eklemeli(list_all)
