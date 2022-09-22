import pandas as pd

df = pd.read_excel("DemonteM20220000000372.xls")


sozluk = df.to_dict("records")

dict_3 = sozluk[133]
print(sozluk)

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



