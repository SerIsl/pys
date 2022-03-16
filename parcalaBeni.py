def parcalaBeni(a):
    if a == "":
        print("Boş Yapmayın!")
    else:
        c = ""

        for w in a: 
            if w.isnumeric():
                c += w

        d = a.partition(c[:4])

        e = []
        f = []
        g = []

        for i in range(len(d)):
            if i == 0:
                for x in d[0]:
                    if x in e:
                        e.append(e.pop()+x)
                        continue
                    e.append(x)
            if i == 1:
                for x in d[1]:
                    f.append(x)
            if i == 2:
                for x in d[2]:
                    if x in g or x.isnumeric():
                        g.append(g.pop()+x)
                        continue
                    g.append(x)

        h = [e, f, g]
        return h


