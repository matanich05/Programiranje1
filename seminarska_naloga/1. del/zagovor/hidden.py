# URL: https://open.kattis.com/problems/hidden

def check(geslo, dolzina_geslo, sporocilo, dolzina_sporoc):
    # Indeksi za spremljanje pozicije v geslu in sporočilu
    index_sporoc = 0
    index_geslo = 0
    # Rezultat (-1 pomeni, da še iščemo)
    rez = -1

    while rez < 0:
        # Če smo prišli do konca sporočila, geslo ni najdeno
        if index_sporoc == dolzina_sporoc:  
            rez = 0
        # Če se znak v sporočilu ujema z znakom v geslu
        elif sporocilo[index_sporoc] == geslo[index_geslo]: 
            index_geslo += 1  # Premaknemo se na naslednji znak v geslu
            # Če smo preverili celo geslo, je bilo najdeno
            if index_geslo == dolzina_geslo:  
                rez = 1
        else:  
            # Preverimo, ali se kateri od naslednjih znakov gesla ujema s trenutnim znakom sporočila
            for i in range(index_geslo + 1, dolzina_geslo):
                if geslo[i] == sporocilo[index_sporoc]:
                    rez = 0  # Geslo ni pravilno
                    break
        # Premaknemo se na naslednji znak v sporočilu
        index_sporoc += 1
    return rez

def main():
    # Preberemo geslo in sporočilo iz vnosa
    geslo, sporocilo = input().split()
    # Shranimo dolžini gesla in sporočila
    dolzina_geslo = len(geslo)
    dolzina_sporoc = len(sporocilo)
    # Pokličemo funkcijo za preverjanje gesla
    result = check(geslo, dolzina_geslo, sporocilo, dolzina_sporoc)
    # Izpišemo PASS, če je geslo najdeno, sicer FAIL
    print("PASS" if result else "FAIL")

# Če program zaženemo neposredno, pokličemo funkcijo main
if __name__ == "__main__":
    main()
