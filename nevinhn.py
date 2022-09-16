import pandas as pd

df = pd.read_excel("DemonteM20220000000372.xls")


sozluk = df.to_dict("records")
dict_3 = sozluk[133]
print(dict_3)
malzeme_kodu = ""

for key, value in dict_3.items():
    Kasa_No = 0
    adet = 0
    if type(value) == float:
        continue
    if key == "Malzeme Kodu":
        malzeme_kodu = value
    elif "Sandık/Miktar" in key:
        Kasa_No = "M" + value.split("/")[0].replace(" ", "")
        adet = value.split("/")[1].replace(" ", "")
        print("Kasa no: " + Kasa_No + " Adet: " + adet + " Malzeme Kodu: "+ malzeme_kodu)
    


