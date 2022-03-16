
all = []
entry = ""
while True:
    entry = input('giriş yap:')
    if entry == "ok":
        break
    
    all.append(int(entry))

all.sort()
print(*all, sep="\n")
print(len(all))

