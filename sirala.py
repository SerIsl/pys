def sirala():
    all = set()
    same = {}
    entry = ""
    mod = int(input("Lütfen Modu seçin (0/1):"))
    while True:
        entry = input('Bitirmek için ok yaz!\ngiriş yap:\t')
        if entry.lower() == "ok":
            break
        
        if mod == 1:
            if entry in all:
                print("Hey dostum bu daha önce girilmiş başka bi tane dene!")
                if entry in same.keys():
                    same[entry] += 1
                else:
                    same[entry] = 1
                continue
            else:
                all.add(entry)
        else: 
            intent = int(entry)
            if intent in all:
                print("Hey dostum bu daha önce girilmiş başka bi tane dene!")
                if intent in same.keys():
                    same[intent] += 1
                else:
                    same[intent] = 1
                continue
            else:
                all.add(intent)
    list_all = list(all)
    list_all.sort()
    print(*list_all, sep="\n")
    print("Toplam kayıt sayısı:", len(list_all))
    print("Benzerler: ", same)
    print("Benzerlerin toplam sayısı: ", sum(list(same.values())))
