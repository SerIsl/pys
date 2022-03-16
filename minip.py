with open("bilgiler.txt", encoding="utf-8") as f:
    with open("gecenler.txt", "w", encoding="utf-8") as g:
        with open("kalanlar.txt", "w", encoding="utf-8") as k:
            icerik = f.readlines()
            m = 0
            for satir in icerik:
                if m == 0:
                    m += 1
                    continue
                satir = satir.replace("\n", "")
                bosluk_sayisi = 0
                bosluk_indexleri = []
                index = 0
                for karakter in satir:
                    if karakter == " ":
                        bosluk_sayisi += 1
                        bosluk_indexleri.append(index)
                    index += 1
                ad_soyad = satir[:bosluk_indexleri[0]]
                soyad = ad_soyad.split("-")[-1]
                ad = ad_soyad[:ad_soyad.index(soyad) - 1].replace("-", " ")
                notlar = satir.split(" ")[-1]
                vize, vize2, final = notlar.split("/")
                ortalama = int(vize) * 0.3 + int(vize2) * 0.3 + int(final) * 0.43
                bolum = satir[bosluk_indexleri[0] + 1 : bosluk_indexleri[-1]]
                if ortalama >= 70 and int(final) >= 70:
                    g.write(ad)
                    g.write(" " * (15 - len(ad)))
                    g.write(soyad)
                    g.write(" " * (15 - len(soyad)))
                    g.write(bolum)
                    g.write(" " * (15 - len(bolum)))
                    g.write(str(round(ortalama, 1)))
                    g.write(" " * (15))
                    g.write("Geçti")
                    g.write("\n")
                else:
                    k.write(ad)
                    k.write(" " * (15 - len(ad)))
                    k.write(soyad)
                    k.write(" " * (15 - len(soyad)))
                    k.write(bolum)
                    k.write(" " * (15 - len(bolum)))
                    k.write(str(round(ortalama, 1)))
                    k.write(" " * (15))
                    k.write("Kaldı")                   
                    k.write("\n")