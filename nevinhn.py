from unicodedata import numeric
import pandas as pd

dosya = "Kopya DemonteM20230000000214.xlsx"

df = pd.read_excel(dosya)


sozluk = df.to_dict("records")

# dict_3 = sozluk[133]
# print(sozluk)

def cells(satir):
    malzeme_kodu = ""
    ürün_adı = ""
    ürün_adı_ing = ""
    mydict1 = []
    
    for key, value in satir.items():
        kasa_no = 0
        adet = 0
        tempdict = {}
        if type(value) != str:
            continue 

        if key == "Malzeme Kodu":
            malzeme_kodu = value
        elif key == "Malzeme Tanımı":
            ürün_adı = value
        elif key == "Malzeme İng.Tanımı":
            ürün_adı_ing = value
        elif "Sandık/Miktar" in key:
            kasa = value.split("/")[0].replace(" ", "")
            if kasa.isnumeric():
                kasa_no = "_"+kasa
            else:
                kasa_no = kasa 
            

            adet = value.split("/")[1].replace(" ", "")
            tempdict["Kasa No"] = kasa_no
            tempdict["malzeme_kodu"] = malzeme_kodu
            tempdict["ürün adı"] = ürün_adı
            tempdict["ürün adı ing"] = ürün_adı_ing
            tempdict["adet"] = adet
            mydict1.append(tempdict)

    return mydict1    
            

a = list(map(cells, sozluk))

c = [x for b in a for x in b]
e =sorted(c, key=lambda x: int(x["Kasa No"][1:]))
d = sorted(e, key=lambda x: x["Kasa No"][0:1])

df_d = pd.DataFrame(d)
df_d.to_excel("nev"+dosya)
print("Dosya başarılı bir şekilde oluşturuldu.")