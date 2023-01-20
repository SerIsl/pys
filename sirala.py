def sirala():
    all = set()
    same = set()
    entry = ""
    mod = int(input("Lütfen Modu seçin (0/1):"))
    while True:
        entry = input('Bitirmek için ok yaz!\ngiriş yap:\t')
        if entry.lower() == "ok":
            break
        
        if mod == 1:
            if entry in all:
                print("Hey dostum bu daha önce girilmiş başka bi tane dene!")
                same.add(entry)
                continue
            else:
                all.add(entry)
        else: 
            if int(entry) in all:
                print("Hey dostum bu daha önce girilmiş başka bi tane dene!")
                same.add(int(entry))
                continue
            else:
                all.add(int(entry))
    list_all = list(all)
    list_same = list(same)
    list_all.sort()
    print(*list_all, sep="\n")
    print("Toplam kayıt sayısı:", len(list_all))
    print("benzerler: ", list_same )
    print("sayısı: ", len(list_same))

