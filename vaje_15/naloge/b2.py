def geslo(napis):
    """Izračuna geslo na podlagi skupnih črk v obeh polovicah niza."""
    dolzina = len(napis) // 2
    prva_polovica = set(napis[:dolzina])
    druga_polovica = set(napis[dolzina:])
    
    # Poiščemo črke, ki se pojavijo v obeh polovicah
    skupne_crke = [crka for crka in prva_polovica if crka in druga_polovica]
    
    vsota = 0
    for crka in skupne_crke:
        if "a" <= crka <= "z":  # Male črke: a = 1, ..., z = 26
            vsota += ord(crka) - ord("a") + 1
        elif "A" <= crka <= "Z":  # Velike črke: A = 27, ..., Z = 52
            vsota += ord(crka) - ord("A") + 27

    return vsota

napis = "hBOLmjuEVBLaBKhcLeqApkRIxREFsf"
print(geslo(napis))
