def protinapad(niz):
    """Vrne niz, ki vsebuje kratice protinapadov glede na napade od pošatsi"""
    napad = "RBL"
    obramba = ""
    i = 0
    while i < len(niz):
        kombinacija = niz[i:i + 3]
        if set(kombinacija) == {"R", "B", "L"}:
            obramba += "C"
            i += 3
        elif niz[i] == "R":
            obramba += ("S")
            i += 1
        elif niz[i] == "B":
            obramba += ("K")
            i += 1
        elif niz[i] == "L":
            obramba += ("H")
            i += 1
    return(obramba)

vhodni_podatek = input()
print(protinapad(vhodni_podatek))