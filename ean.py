def ean_kontrol(ean=None):

    if ean is None or len(ean)<13:
        ean = input("Ean kodunu giriniz:\t")
    
    
    tek = 0
    cift = 0
    for i in range(len(ean)-1):
        if i % 2 == 0:
            cift += int(ean[i])
        else:
            tek += int(ean[i])
        
    kontrol_no = 10 - ((tek * 3 + cift)%10)

    if kontrol_no == 10:
        kontrol_no = 0
    


    if kontrol_no == int(ean[-1]):
        print(f"Girdiğiniz Ean numarası doğru. Ean:\t {ean}")
    else:
        print(f"Girilen Ean numarası yanlış. Olması gereken Ean numarası: {ean[:-1]+str(kontrol_no)}")


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

# ean_olusturmak()
# ean_kontrol()