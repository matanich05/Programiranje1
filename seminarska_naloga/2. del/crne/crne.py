    def rezanje(n):
        """Vrne na koliko delov se bo šahovnica razrezala"""
        horizontalni_rez = n // 2
        navpicni_rez = n - horizontalni_rez
        vrstice = horizontalni_rez + 1
        stolpci = navpicni_rez + 1
        kosi = vrstice * stolpci
        rezultat = kosi
        return rezultat
    n = int(input())
    print(rezanje(n))
