# URL: https://open.kattis.com/problems/headguard

def s_vrstica(linija):
    # Seznam za shranjevanje rezultatov
    rez = []
    # Števec enakih znakov
    stevec = 1

    # Gremo skozi vse znake v vrstici (od drugega naprej)
    for i in range(1, len(linija)):
        # Če je znak enak prejšnjemu, povečamo števec
        if linija[i] == linija[i - 1]:
            stevec += 1
        else:
            # Dodamo število ponovitev in znak v seznam
            rez.append(f"{stevec}{linija[i - 1]}")
            # Ponastavimo števec na 1
            stevec = 1

    # Dodamo zadnji znak in njegovo število ponovitev
    rez.append(f"{stevec}{linija[-1]}")
    # Združimo vse v en niz in vrnemo rezultat
    return ''.join(rez)

def main():
    # Seznam za shranjevanje vnosov
    linije = []
    while True:
        try:
            # Preberemo vrstico in odstranimo presledke okoli nje
            linija = input().strip()
            # Če je vrstica prazna, končamo branje
            if not linija:
                break
            # Shranimo vrstico v seznam
            linije.append(linija)
        except EOFError:
            # Če pridemo do konca vnosa, končamo
            break

    # Gremo skozi vse vrstice in jih obdelamo
    for linija in linije:
        print(s_vrstica(linija))

# Če program zaženemo neposredno, pokličemo funkcijo main
if __name__ == "__main__":
    main()
