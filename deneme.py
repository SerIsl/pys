
modeller = {
    "Y" : "Soft Dizayn",
    "X" : "Wind Dizayn",
    "T" : "Titanyum Dizayn",
    "C" : "Gold Dizayn",
    "Q" : "Qubic Dizayn",
    "A" : "Arc Dizayn",
    "F" : "Flat Dizayn",
    "H" : "ELITE Dizayn",
    "K" : "KÜP(CUBE) Dizayn"
}

ozellikler = {
    "G" : "Gazlı",
    "GG" : "Gazlı Grilli",
    "D" : "Doğal Gazlı",
    "S" : "Emniyet Ventili",
    "E" : "Elektrikli Resistans",
    "SS" : "Full Emniyetli",
    "s" : "Üst table emniyetli(Gazlı Fırınlarda)",

}

while True: 
    isim = input("Giriş yap: ")
    liste = []
    if isim.lower() == "q":
        break
    for i in isim:
    
        if len(liste) > 8 and liste[-1] == i:
            c = liste.pop()
            liste.append(c+i)
            continue
    
        if i in liste and len(liste) > 8 and not i.isnumeric():
            liste.append(i)
            continue
    
        if i in liste and not i.isnumeric() and 1 < len(liste) < 8:
            b = liste.pop()
            liste.append(b+i)
            continue

        if len(liste) >	 8 and i.isnumeric() :
            a = liste.pop()
            liste.append(a+i)
            continue
    
        liste.append(i)
    sayac = 0
    firin = ""
    for i in liste: 
        if sayac == 0:
            firin += modeller.get(i) + "\n"
        elif 0< sayac < 4 :
            firin += str(ozellikler.get(i)) + "\n"
	
        sayac += 1
        
             	
    print(firin)
    print(sayac)
    print(type(ozellikler.get("s")))
                 