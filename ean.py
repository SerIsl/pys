while True:
    ean = input("Sayı giriniz:\t")
    if ean.lower() == "ok":
        break

    tek = 0
    cift = 0

    for i in range(len(ean)):
        if i % 2 == 0:
            cift += int(ean[i])
        else:
            tek += int(ean[i])

    ean_kontrol_no = 10-((tek*3+cift)%10)
    
    if ean_kontrol_no == 10:
        ean_kontrol_no = 0

    ean_no = ean + str(ean_kontrol_no)
    print(ean_no)