def protinapad(niz):
    obramba = []
    i = 0
    dolzina = len(niz)
    while i < dolzina:
        if i + 2 < dolzina:
            c1, c2, c3 = niz[i], niz[i+1], niz[i+2]
            if 'R' in (c1, c2, c3) and 'B' in (c1, c2, c3) and 'L' in (c1, c2, c3):
                obramba.append('C')
                i += 3
                continue
        if niz[i] == 'R':
            obramba.append('S')
        elif niz[i] == 'B':
            obramba.append('K')
        else:
            obramba.append('H')
        i += 1
    return ''.join(obramba)

vhodni_podatek = input().strip()
print(protinapad(vhodni_podatek))
