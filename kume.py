st = set()

sa = 0

while True:

    a = input("Model numarasını giriniz:\t")

    if a.lower() == "ok":
        break
    else:
        print("Lütfen çıkmak ve/veya sonladırmak için 'ok' yazınız!!")
    
    st.add(a) 
    
    

    print(st)
    print(len(st))

