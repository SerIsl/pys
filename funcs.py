def isEmri(val):
  a = val[-5:]
  return a
  

def seriNum(barkod, isemri, hafta, adet):
    s = f"{barkod}M{isemri}22{hafta}{adet:>04}"
    print(s)
    print(len(s))
    print()  





