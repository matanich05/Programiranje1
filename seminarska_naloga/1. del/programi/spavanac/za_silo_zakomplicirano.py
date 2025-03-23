def premakni_cas(ura, minuta):
    # Pretvorimo uro in minuto v skupno število minut
    skupne_minute = ura * 60 + minuta - 45  # Premaknemo čas za 45 minut nazaj

    # Če smo šli pod 0 minut, dodamo 1440 (cel dan), da ostanemo v okviru 24 ur
    if skupne_minute < 0:
        skupne_minute += 1440

    # Izračunamo novo uro in minute
    nova_ura = skupne_minute // 60
    nove_minute = skupne_minute % 60

    # Vrnemo novo uro in minute
    return nova_ura, nove_minute

def glavna_funkcija():
    # Preberemo uro in minute iz vnosa
    ura, minuta = map(int, input().split())

    # Premaknemo čas nazaj za 45 minut
    nova_ura, nove_minute = premakni_cas(ura, minuta)

    # Izpišemo novo uro in minute
    print(nova_ura, nove_minute)

# Zaženemo program, če ga izvajamo neposredno
if __name__ == "__main__":
    glavna_funkcija()
