### Tega dela kode ne spreminjaj! ###
with open('B1_kraji.txt', 'r') as datoteka:
    kraji = datoteka.read()
    seznam_krajev = kraji.split(' ')

def najdi_najboljsi_kraj(kraji):
    """Najde kraj z najboljšim razmerjem med samoglasniki in soglasniki."""
    samoglasniki = "aeiou"
    naj_kraj = ""
    max_razmerje = -1  

    for kraj in kraji:
        st_samoglasnikov = 0
        st_soglasnikov = 0

        # Preštejemo samoglasnike in soglasnike
        for crka in kraj.lower():
            if crka in samoglasniki:
                st_samoglasnikov += 1
            elif crka.isalpha():  # Ignoriramo znake, ki niso črke
                st_soglasnikov += 1

        # Izračunamo razmerje, če kraj vsebuje soglasnike
        if st_soglasnikov > 0:
            razmerje = st_samoglasnikov / st_soglasnikov
            if razmerje > max_razmerje:  # Posodobimo, če je razmerje boljše
                max_razmerje = razmerje
                naj_kraj = kraj

    return naj_kraj

print(najdi_najboljsi_kraj(seznam_krajev))
