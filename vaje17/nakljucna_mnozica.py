import random
import time

def gen_stevilo1(n):
    """Vrne množico naključno izbranih števil med 1 in 100, dolžine n"""
    mnozica = set()
    while len(mnozica) < n:
        mnozica.add(random.randint(1, 100))
    return mnozica

def gen_stevilo2(n):
    """Vrne množico, ki je razlika množice števil od 1 do 100
    in množice, katere dolžina je 100-n in vsebuje elemente med 1 in 100"""
    vsi = set(range(1, 101))
    izkljuceni = set()
    vel = 100 - n
    while len(izkljuceni) < vel:
        izkljuceni.add(random.randint(1, 100))
    return vsi - izkljuceni

def gen_stevilo3(n):
    """Generira množico števil od 1 do 100, dolžine n"""
    izkljuceni = set(random.sample(range(1, 101), n))
    return izkljuceni

def cas(fun, n):
    """Izmeri čas potreben, da se funkcija izvede n-krat"""
    zac_cas = time.time()
    for _ in range(1000):
        fun(n)
    kon_cas = time.time()
    povp_cas = (kon_cas - zac_cas) / 1000
    return povp_cas

def gen_stevilo(n):
    cas = time.time()
    if n < 50:
        gen_stevilo1(n)
    else:
        gen_stevilo2(n)
    return abs(cas - time.time())

n = 10
print("n = 10")
fun = gen_stevilo1
print(f"Povprečni čas funkcije gen_stevilo1 je {cas(fun, n)}")
fun = gen_stevilo2
print(f"Povprečni čas funkcije gen_stevilo1 je {cas(fun, n)}")
fun = gen_stevilo3
print(f"Povprečni čas funkcije gen_stevilo1 je {cas(fun, n)}")

n = 50
print("n = 50")
fun = gen_stevilo1
print(f"Povprečni čas funkcije gen_stevilo1 je {cas(fun, n)}")
fun = gen_stevilo2
print(f"Povprečni čas funkcije gen_stevilo1 je {cas(fun, n)}")
fun = gen_stevilo3
print(f"Povprečni čas funkcije gen_stevilo1 je {cas(fun, n)}")

n = 90
print("n = 90")
fun = gen_stevilo1
print(f"Povprečni čas funkcije gen_stevilo1 je {cas(fun, n)}")
fun = gen_stevilo2
print(f"Povprečni čas funkcije gen_stevilo1 je {cas(fun, n)}")
fun = gen_stevilo3
print(f"Povprečni čas funkcije gen_stevilo1 je {cas(fun, n)}")
