# Preberemo število testnih primerov
t = int(input())

# Ponovimo za vsak testni primer
for _ in range(t):
    # Preberemo število besed
    n = int(input())
    # Slovar za prevode iz tujega v domači jezik
    tuji_domac = {}
    # Slovar za prevode iz domačega v tuji jezik
    domac_tuji = {}

    # Gremo skozi vse besede
    for i in range(n):
        # Preberemo ime (ne uporabljamo ga)
        ime = input()
        # Preberemo tuje besede in odstranimo prvo besedo (ker je ime)
        tuji = input().split()[1:]
        # Preberemo domače besede in odstranimo prvo besedo (ker je ime)
        domac = input().split()[1:]

        # Shranimo povezave iz tujega v domači jezik
        for beseda in tuji:
            dom_pomen = set(domac)
            # Če beseda že obstaja v slovarju, poiščemo skupne pomene
            if beseda in tuji_domac:
                tuji_domac[beseda] = tuji_domac[beseda].intersection(dom_pomen)
            else:
                tuji_domac[beseda] = dom_pomen

        # Shranimo povezave iz domačega v tuji jezik
        for beseda in domac:
            tuj_pomen = set(tuji)
            # Če beseda že obstaja v slovarju, poiščemo skupne pomene
            if beseda in domac_tuji:
                domac_tuji[beseda] = domac_tuji[beseda].intersection(tuj_pomen)
            else:
                domac_tuji[beseda] = tuj_pomen

    # Pridobimo vse tuje besede in jih uredimo po abecedi
    keys = list(tuji_domac.keys())
    keys.sort()

    # Gremo skozi vsako tujo besedo
    for k in keys:
        pomen = []
        # Poiščemo vse ustrezne domače prevode
        for fn in tuji_domac[k]:
            # Preverimo, ali je prevod dvosmeren
            if k in domac_tuji[fn]:
                pomen.append(fn)
        # Uredimo prevode po abecedi
        pomen.sort()
        # Izpišemo pare besed
        for m in pomen:
            print('(' + k + ', ' + m + ')')

    # Če ni zadnji testni primer, izpišemo prazno vrstico
    if _ != t - 1:
        print()
