def sirala():
    all = []
    entry = ""
    while True:
        entry = input('Bitirmek için ok yaz!\ngiriş yap:\t')
        if entry == "ok":
            break
        
        if int(entry) in all:
            print("Bu kayıt daha önce girilmiş başka bir sayı ile tekrar dene!")
            continue
        else:    
            all.append(int(entry))

    all.sort()
    print(*all, sep="\n")
    print("Toplam kayıt sayısı:", len(all))

