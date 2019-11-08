def unitPropagate(s, i):
    contador = 0
    unitaria = True
    while "" not in s and unitaria:
        print(s)
        check = 0
        for l in s:
            if (len(l) > 2 or (len(l) == 2 and l[0] != "-")):
                check += 1
        if check == len(s):
            unitaria = False
        if contador >= len(s):
            break
        elif s[contador] == "":
            contador += 1
        elif len(s[contador]) == 1:
            prop = s[contador]
            i[prop] = 1
            p = s.copy()
            for c in s:
                print(c)
                if prop in c and "-"+ prop not in c:
                    p.remove(c)
                elif "-" + prop in c:
                    p.remove(c)
                    p.append(c[:c.index(prop)-1] + c[c.index(prop)+1:])
            s = p
        elif len(s[contador]) == 2 and s[contador][0] == "-":
            prop = s[contador]
            i[prop[1:]] = 0
            p = s.copy()
            for c in s:
                if prop in c:
                    p.remove(c)
                elif prop[1] in c:
                    p.remove(c)
                    p.append(c[:c.index(prop[1])] + c[c.index(prop[1])+1:])
            s = p
    return (s, i)

d = {"p": 0, "q": 1}
(s, i) = unitPropagate(["q", "-q"], d)
print(s,i)
