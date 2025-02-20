def vsota_stevk(n):
    """
    Vrne vsoto števk naravnega števila n
    """
    vsota = 0
    while n > 0:
        vsota += n % 10
        n //= 10
    return vsota


def lazji(x, y):
    """
    Vrne True, če je vsota števk x manjša ali enaka vsoti števk y
    Tako x kot y sta naravni števili
    """
    return vsota_stevk(x) <= vsota_stevk(y)


def uredi_od_lazji_do_tezji(podatki):
    """uredi_od_lazji_do_tezji tabelo s števili po vsoti njihovih števk z uporabo te funkcije"""
    
    if len(podatki) <= 1:
        return podatki
    zacetni_el = podatki[0]
    lazji_el = [x for x in podatki[1:] if lazji(x, zacetni_el)]
    tezji_el = [x for x in podatki[1:] if not lazji(x, zacetni_el)]
    rezultat = uredi_od_lazji_do_tezji(lazji_el) + [zacetni_el] + uredi_od_lazji_do_tezji(tezji_el)
    return rezultat



# TESTI
print("TESTNI PRIMERI (Razvrstitev od najlažjega do najtežjega):")
print("------------------------------------------------------------------------------------------------------------------------------------------------")
podatki = []
print(f"Pričakovan rezultat: [], rešitev programa: {uredi_od_lazji_do_tezji(podatki)}")
print("------------------------------------------------------------------------------------------------------------------------------------------------")
podatki = [1]
print(f"Pričakovan rezultat: [1], rešitev programa: {uredi_od_lazji_do_tezji(podatki)}")
print("------------------------------------------------------------------------------------------------------------------------------------------------")
podatki = [1, 2, 3, 4, 5, 6, 7]
print(f"Pričakovan rezultat: [1, 2, 3, 4, 5, 6, 7], rešitev programa: {uredi_od_lazji_do_tezji(podatki)}")
print("------------------------------------------------------------------------------------------------------------------------------------------------")
podatki = [1, 1, 1, 1, 1, 1, 1]
print(f"Pričakovan rezultat: [1, 1, 1, 1, 1, 1, 1], rešitev programa: {uredi_od_lazji_do_tezji(podatki)}")
print("------------------------------------------------------------------------------------------------------------------------------------------------")
podatki = [23, 67, 45, 987, 345243265, 234, 346, 123, 567, 3]
print(f"Pričakovan rezultat: [3, 23, 123, 234, 45, 346, 67, 567, 987, 3452433265], rešitev programa: {uredi_od_lazji_do_tezji(podatki)}")
print("------------------------------------------------------------------------------------------------------------------------------------------------")
podatki = [1536616, 3462767, 42, 2162364, 410004544422, 3426547, 235747, 4444427, 25775]
print(f"Pričakovan rezultat: [42, 2162364, 25775, 235747, 1536616, 4444427, 410004544422, 3426547, 3462767], rešitev programa: {uredi_od_lazji_do_tezji(podatki)}")
print("------------------------------------------------------------------------------------------------------------------------------------------------")
