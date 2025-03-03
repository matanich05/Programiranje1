def collatz(n):
    """Vrne število korakov do 1 v Collatzovem zaporedju."""
    koraki = 0  

    while n > 1:
        if n % 2 == 0:  # Sodo število delimo z 2
            n //= 2
        else:  # Liho število pomnožimo s 3 in prištejemo 1
            n = n * 3 + 1
        koraki += 1  # Štejemo korake

    print(koraki)
    return koraki

collatz(2318)
