import math

def najdi_liho_prastevilo(stevilo):
    """Vrne najmanjše liho praštevilo, ki deli število."""
    for i in range(3, stevilo + 1, 2):  # Preverjamo le liha števila
        if stevilo % i == 0 and preveri_prastevilo(i):
            return i

def preveri_prastevilo(n):
    """Preveri, ali je število praštevilo."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  # Deljenje do kvadratnega korena
        if n % i == 0:
            return False
    return True

def izracunaj_vsoto_stevk(stevilo):
    """Izračuna vsoto števk izraza (stevilo * 100 - stevilo)."""
    vrednost = (stevilo * 100) - stevilo
    return sum(int(stevka) for stevka in str(vrednost))

def program():
    prvo_stevilo = int(input())
    drugo_stevilo = int(input())
    prastevilo = najdi_liho_prastevilo(prvo_stevilo)
    vsota_stevk = izracunaj_vsoto_stevk(drugo_stevilo)
    print(str(prastevilo) + str(vsota_stevk))

program()
