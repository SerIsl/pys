def ean_kontrol(ean):
    tek = 0
    cift = 0
    for i in range(len(ean)):
        if i % 2 == 0:
            cift += int(ean[i])
        else:
            tek += int(ean[i])
        
    kontrol_no = 10 - ((tek * 3 + cift)%10)

    if kontrol_no == ean[-1]:
        print(f"Girdiğiniz Ean numarası doğru. Ean:\t {ean}")
    else:
        print("Girilen Ean numarası yalnış.")


def ean_olusturmak(): 
    while True:
        ean = input("Sayı giriniz:\t")
        if ean.lower() == "ok":
            break
        elif len(ean) < 12:
            print(f"Girdiğiniz sayı en az 12 basamaklı olmalıdır. Girilen sayı {len(ean)} basamaklı.")
            continue
        elif len(ean) > 12:
            print(f"Girdiğiniz sayı 12 basamaktan fazla. Girilen sayı {len(ean)} basamaklı.")
            continue
        elif not ean.isnumeric():
            print("12 basamaklı bir sayı giriniz.")
            continue

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