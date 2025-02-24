def a1(stevilo):
    vsota = 0
    for n in range(1, stevilo):
        if stevilo % n == 0:
            vsota += n
    if vsota == stevilo:
        return stevilo / 3
    elif abs(vsota - stevilo) <= 2:
        return vsota // 7
    else:
        return vsota // 14

#stevilo = 8589934592
stevilo = int(input(""))
print(a1(stevilo))
