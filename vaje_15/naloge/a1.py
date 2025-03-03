import math

def vrsta_stevila(stevilo):
    """Določi vrsto števila glede na vsoto deliteljev."""
    
    vsota = 0  # Vsota deliteljev

    # Poiščemo delitelje do kvadratnega korena
    for i in range(1, int(math.sqrt(stevilo)) + 1):
        if stevilo % i == 0:
            vsota += i
            if i != 1 and i != stevilo // i:  # Izognemo se dvojnikom
                vsota += stevilo // i  

    razlika = abs(vsota - stevilo)  # Odstopanje od vsote deliteljev

    # Določimo vrsto števila glede na razliko
    if razlika == 0:
        return stevilo // 3
    elif razlika <= 2:
        return vsota // 7
    else:
        return vsota // 14

print(vrsta_stevila(8589934592))
