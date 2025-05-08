import turtle

def nKotnik(risi, n, stranica, barva):
    """Nariše n-kotnik pobarvan s stranico dolžine stanica in barvo barva"""
    risi.fillcolor(barva)
    risi.begin_fill()
    for _ in range(n):
        risi.fd(stranica)
        risi.rt(360 / n)
    risi.end_fill()

stranice = int(input('Napiši število stranic lika: '))
dolzina = int(input('Napiši dolžino stranice: '))
barva = input('Napiši barvo s katero naj bo pobarvana notranjost lika: ')
x = turtle.Turtle()

nKotnik(x, stranice, dolzina, barva)
        