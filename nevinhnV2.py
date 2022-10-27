
from numpy import nan
import pandas as pd

dosya = "PR-220919-AG PROLUX 1200 TK BL 19.10.2022.xlsx"

df = pd.read_excel(dosya, dtype=str)


sozluk = df.to_dict("records")

# dict_3 = sozluk[133]
# print(sozluk)

def cells(satir):
    malzeme_kodu = ""
    ürün_adı = ""
    ürün_adı_ing = ""
    mydict1 = []
    tmp = []
    
    for key, value in satir.items():
    
        tempdict = {}
        if type(value) == float:
            continue 

        if "CODE" in key:
            malzeme_kodu = value
        elif "TR" in key:
            ürün_adı = value
        elif "ENG" in key:
            ürün_adı_ing = value
        elif "SANDIK NO" in key:
            if value.isnumeric():
                tmp.append('M'+str(value))
            else:
                tmp.append(value)
        elif "ADET" in key:

            tempdict["Kasa No"] = tmp.pop()
            tempdict["Malzeme Kodu"] = malzeme_kodu
            tempdict["Ürün Adı"] = ürün_adı
            tempdict["Ürün Adı İng"] = ürün_adı_ing
            tempdict["Adet"] = value
            mydict1.append(tempdict)

    return mydict1    
            

a = list(map(cells, sozluk))

c = [x for b in a for x in b]
e =sorted(c, key=lambda x: int(x["Kasa No"][1:]))
d = sorted(e, key=lambda x: x["Kasa No"][0:1])

df_d = pd.DataFrame(d)
df_d.to_excel("nevV2"+dosya)
print("Dosya başarılı bir şekilde oluşturuldu.")