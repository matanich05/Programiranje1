# URL: https://open.kattis.com/problems/parentgap

def prestopno_leto(y):
    """Vrne True, če je leto prestopno, sicer False."""
    # Leto je prestopno, če je deljivo s 400 ali če je deljivo s 4, a ne s 100
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

def mesec_dnevi(mesec, y):
    """Vrne število dni v določenem mesecu glede na leto."""
    # Seznam dni v mesecih (februar ima 28 dni)
    dnevi = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # Če je leto prestopno in je mesec februar, vrnemo 29 dni
    if mesec == 2 and prestopno_leto(y):
        return 29
    # Vrnemo ustrezno število dni v mesecu
    return dnevi[mesec - 1]

def dan_v_tednu(dan, mesec, leto):
    """Vrne dan v tednu za določen datum."""
    # Število dni od začetka leta
    dnevi_vsi = dan
    # Dodamo dni prejšnjih mesecev
    for m in range(1, mesec):
        dnevi_vsi += mesec_dnevi(m, leto)
    # Dodamo dni prejšnjih let (upoštevamo prestopna leta)
    dnevi_vsi += (leto - 1) * 365 + (leto - 1) // 4 - (leto - 1) // 100 + (leto - 1) // 400
    # Vrnemo ostanek pri deljenju s 7 (0 = nedelja, 1 = ponedeljek, ...)
    return dnevi_vsi % 7

def druga_nedelja(mesec, leto):
    """Vrne datum druge nedelje v mesecu."""
    # Poiščemo prvi dan meseca
    prvi_dan = dan_v_tednu(1, mesec, leto)
    # Poiščemo prvo nedeljo (premikamo se do prve nedelje v mesecu)
    prvi_nedelja = 1 + (7 - prvi_dan) % 7
    # Druga nedelja je 7 dni po prvi nedelji
    return prvi_nedelja + 7

def tretja_nedelja(mesec, leto):
    """Vrne datum tretje nedelje v mesecu."""
    # Najprej poiščemo drugo nedeljo v mesecu
    drugi_nedelja = druga_nedelja(mesec, leto)
    # Tretja nedelja je 7 dni po drugi nedelji
    return drugi_nedelja + 7

def parent_gap(y):
    """Izračuna in izpiše razmik med materinskim in očetovim dnem."""
    # Materinski dan je druga nedelja v maju
    mati_dan = druga_nedelja(5, y)
    # Očetovski dan je tretja nedelja v juniju
    oce_dan = tretja_nedelja(6, y)
    # Izračunamo število tednov med njima
    razmak = (oce_dan + mesec_dnevi(5, y) - mati_dan) // 7
    # Izpišemo rezultat
    print(f"{razmak} weeks")

# Preberemo leto iz vnosa
y = int(input())
# Izračunamo in izpišemo razmik med materinskim in očetovim dnem
parent_gap(y)
