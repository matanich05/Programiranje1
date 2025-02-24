import math

def a1(stevilo):
    vsota = 0
    for n in range(1, int(math.sqrt(stevilo)) + 1):
        if stevilo % n == 0:
            vsota += n
            if n != 1 and n != stevilo // n:
                vsota += stevilo // n
    
    if vsota == stevilo:
        return stevilo // 3
    elif abs(vsota - stevilo) <= 2:
        return vsota // 7
    else:
        return vsota // 14

stevilo = 8589934592
print(a1(stevilo))

