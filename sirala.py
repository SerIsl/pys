def sirala():
    all = set()
    entry = ""
    mod = int(input("Lütfen Modu seçin (0/1):"))
    while True:
        entry = input('Bitirmek için ok yaz!\ngiriş yap:\t')
        if entry.lower() == "ok":
            break
        
        if mod == 1:
            all.add(entry)
        else:    
            all.add(int(entry))
    list_all = list(all)
    list_all.sort()
    print(*all, sep="\n")
    print("Toplam kayıt sayısı:", len(all))