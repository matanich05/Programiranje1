def main():
    # Preberemo število vozlišč
    n = int(input().strip())
    
    # Poseben primer: če je samo eno vozlišče, je rezultat 1.0
    if n == 1:
        print("1.0")
        return

    # Pripravimo seznam sosedov (1-indeksiran)
    sosedi = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        sosedi[u].append(v)
        sosedi[v].append(u)
    
    # Izračunamo stopnjo vsakega vozlišča (število sosedov)
    stopnja = [0] * (n + 1)
    for i in range(1, n + 1):
        stopnja[i] = len(sosedi[i])
    
    skupna_kaskadna = 0.0

    # Za vsako vozlišče izvedemo BFS in izračunamo kaskadno centralnost
    for i in range(1, n + 1):
        # Inicializiramo sezname za produkt stopenj in obiskana vozlišča
        produkt = [0.0] * (n + 1)
        obiskano = [False] * (n + 1)
        
        # Za vozlišče i nastavimo začetno vrednost
        produkt[i] = 1.0
        obiskano[i] = True
        
        # Uporabimo seznam kot vrsto (queue)
        vrsta = [i]
        
        while len(vrsta) > 0:
            cur = vrsta.pop(0)
            for sos in sosedi[cur]:
                if not obiskano[sos]:
                    obiskano[sos] = True
                    if cur == i:
                        # Če je sosed neposredno povezan z začetnim vozliščem
                        produkt[sos] = float(stopnja[sos])
                    else:
                        # Razbijemo izraz na več vrstic za jasnost
                        produkt[sos] = (
                            produkt[cur] *
                            stopnja[sos]
                        )
                    vrsta.append(sos)
        
        # Izračunamo vsoto 1/produkt[j] za vsa j, kjer j ni i
        vsota = 0.0
        for j in range(1, n + 1):
            if j != i:
                vsota += 1.0 / produkt[j]
        
        # Kaskadna centralnost vozlišča i je 1 + vsota
        kaskadna = 1.0 + vsota
        skupna_kaskadna += kaskadna
    
    # Izračunamo povprečje kaskadnih centralnosti
    povprecje = skupna_kaskadna / n
    print(f"{povprecje:.9f}")

if __name__ == "__main__":
    main()
