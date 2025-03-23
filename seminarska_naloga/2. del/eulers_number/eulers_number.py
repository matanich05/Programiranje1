import math

def eulerjevo_stevilo(n):
    """Vrne realno število približek števila e, za dani n po formuli"""
    stevec = 1.0   # števec je vedno enak, tako da lahko vsakič delimo z i + 1
    stevilo = 1.0   # Ker je 1/0! = 1
    for i in range(1, n + 1):
        stevec /= i
        stevilo += stevec
    return stevilo

n = int(input())
print(eulerjevo_stevilo(n))