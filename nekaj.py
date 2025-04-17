def stejHanoi(n):
    """Hanoiski stolpici"""
    if n == 0:
        return 0
    rez = 2 ** n - 1
    return rez

for n in range(1, 16):
    print(f"Za {n} diskov potrebujemo {stejHanoi(n)} premikov")
    