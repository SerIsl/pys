
from parcalaBeni import *

modeller = {
    'Y': 'Soft Dizayn',
    'X': 'Wind Diyazyn',
    'T': 'Titantum Dizayn',
    'C': 'Gold Dizayn',
    'Q': 'Qubic Dizayn',
    'A': 'Arc Dizayn',
    'F': 'Flat Dizayn',
    'H': 'Elite Dizayn',
    'K': 'KÜP(CUBE) Dizayn'
}

tanim = {
    'G': 'Gazlı',
    'GG': 'Gazlı Grilli',
    'D': 'Doğalgazlı',
    'S': 'Emniyet Ventili',
    'E': 'Elektrikli Gril Resistans',
    'SS': 'Full Emniyetli',
    's': 'Üst Table Emniyetli (Gazlı Fırınlarda)'
}

binlerB = {
    '1': "50x50 Fırın",
    '2': "50x60 Fırın",
    '3': "60x60 Üç Katlı Fırın",
    '7': "60x60 Fırın 4 Gözlü",
    '6': "60x60 Çift Katlı Fırın",
    '8': "60x60 Fırın 4 Gözlü",
    '5': "50x60 Çift Katlı Fırın",
    '9': "90x60 Fırın"
}

yuzlerB = {
    '0': 'Normal Elektrikli (Statik Fırın)',
    '2': 'Termostatlı (Statik fırın)',
    '3': 'Turbo Motorlu, Termostatlı (Alt-Üst rezistans)',
    '4': 'Alt-üst Grilli, Turbo Rez., Turbo fan,Thermostatlı',
    '5': 'Alt Gazlı,Turbolu,Thermostatsız'
}

birlerB = {
    '0': 'Çakmaksız',
    '1': 'Butondan Çakmaklı',
    '2': 'Düğmeden Çakmaklı',
    '3': 'Full Butondan Çakmaklı (Gazlı)',
    '4': 'Full Düğmeden Çakmaklı (Gazlı)'
}

harfTanimi = {
    'A': 'Aluminyum Profilli Ön Kapı',
    'a': 'Altın rengi',
    'B': 'Mavi Boya',
    'B1': 'Okyanus Mavisi',
    'B2': 'Lacivert',
    'b': 'Sarı Bek Kapaklı (Brass)',
    'C': 'Çekmece',
    'c': 'Bakır (copper) rengi',
    'D': 'Dijital Timer (Saat)',
    'D1': 'Dokunmatik Dijital Timer (Saat)',
    'e': 'Eskişehir Bekli',
    'F': 'Flap Kapaklı',
    'G': 'Üst Cam Kapaklı (Glass)',
    'g': 'Securit cam',
    'K': 'Siyah Boya',
    'K1': 'Mat Siyah Boya',
    'K2': 'Antresit Boya',
    'K3': 'Mat Antresit Boya',
    'k': 'Üst Tabla Siyah Emaye',
    'k1': 'Üst Tabla Mat Siyah Emaye',
    'k2': 'Üst Tabla Aynalı Emaye',
    'L': 'Lamba',
    'M': 'Multigazlı (Sabaf Bekli)',
    'm': 'İmitasyon Bek',
    'N': 'Nostalji Kapılı',
    'O': 'Kırmızı Boya',
    'O1': 'Parlak Kırmızı Boya',
    'o': 'Pembe Boya',
    'P': 'Kahverengi Boya',
    'P1': 'Ön Panel ve Alt Kapak Ahşap Desen',
    'p': 'Mor Boya',
    'p1': 'TDF renkli üst tabla',
    'R': 'Gri Boya',
    'R1': 'Gümüş Gri Boya',
    'r': 'Alt Çekmece Gri',
    'r1': 'Üst Tabla Gri Emaye',
    'S': 'Yarı Paslanmaz (Stainless)',
    'SS': 'Full Paslanmaz (Stainless)',
    's': 'Sadece Üst Tabla Paslanmaz (Stainless)',
    'ss': 'Sadece Üst Tabla ve Panel Paslanmaz (Stainless)',
    'T': 'Piliç Çevirmeli (Turn speed)',
    't': 'Mekanik Timer (saat)',
    'U': 'Krem Boya',
    'V': 'Wok Bek',
    'v': 'Vitro ceran',
    'Y': 'Yeşil Boya',
    'Y1': 'Parlak Yeşil Boya',
    'Y2': 'Fıstık Yeşili Boya',
    'y': 'Sarı Boya',
    'y1': 'Turuncu Boya',
    'Z': 'Akıllı Bek Gözü',
    'z': 'Akıllı Gazlı Fırın2',
    'Q': 'Rustik'
}
giris=input("Giriş Yapın: ")
a = parcalaBeni(giris)
m = "\n"
for i in range(len(a)):
    if i == 0:
        for x in range(len(a[i])):
            if x == 0:
                m += modeller.get(a[i][x]) + '\n'
            else:
                m += tanim.get(a[i][x]) + '\n'
            continue
    if i == 1:
        for x in range(len(a[i])):
            if x == 0:
                m += binlerB.get(a[i][x]) + '\n'
            elif x == 1:
                m += yuzlerB.get(a[i][x]) + '\n'
            elif x == 2:
                if a[i][x] == '0':
                    m += 'Hot Platesiz\n'
                else:
                    m += a[i][x] + ' Hot Plateli\n'
            elif x == 3:
                m += birlerB.get(a[i][x]) + '\n'
    if i == 2:
        for x in range(len(a[i])):
            m += harfTanimi.get(a[i][x]) + '\n'


print(m, end="")
