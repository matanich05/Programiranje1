import turtle


d = 50

def prva(risi, dolzina, barva_notranjosti):
    """Nariše puščico obrnjeno navzgor"""
    risi.fillcolor(barva_notranjosti)
    risi.begin_fill()
    x.fd(d)
    x.lt(90)
    x.fd(d + d / 2)
    x.rt(90)
    x.fd(d / 2)
    x.lt(120)
    x.fd(2 * d)
    x.lt(120)
    x.fd(2 * d)
    x.lt(120)
    x.fd(d / 2)
    x.rt(90)
    x.fd(d + d / 2)
    x.lt(90)
    risi.end_fill()
    
def druga(risi, dolzina, barva_notranjosti):
    """Nariše puščico obrnjeno navzdol"""
    risi.fillcolor(barva_notranjosti)
    risi.begin_fill()
    x.lt(60)
    x.fd(2 * d)
    x.lt(120)
    x.fd(d / 2)
    x.rt(90)
    x.fd(d + d / 2)
    x.lt(90)
    x.fd(d)
    x.lt(90)
    x.fd(d + d / 2)
    x.rt(90)
    x.fd(d / 2)
    x.lt(120)
    x.fd(2 * d)
    x.lt(60)
    risi.end_fill()
    
def tretja(risi, dolzina, barva_notranjosti):
    """Nariše puščico drugačne oblike kot funkciji prva in druga, ki je usmerjena v desno"""
    risi.fillcolor(barva_notranjosti)
    risi.begin_fill()
    x.rt(90)
    x.fd(d)
    x.lt(90)
    x.fd(3 * d)
    x.rt(150)
    x.fd(d + d / 2)
    x.lt(110)
    x.fd(d / 2 + d / 3)
    x.lt(70)
    x.fd(4 * d)
    x.lt(120)
    x.fd(4 * d)
    x.lt(70)
    x.fd(d / 2 + d / 3)
    x.lt(110)
    x.fd(d + d / 2)
    x.rt(150)
    x.fd(3 * d)
    x.lt(90)
    x.fd(d / 2)
    risi.end_fill()

st = int(input('Izberi obliko puščice (napiši številko od 1 do 3): '))

if st > 3 or st < 1:
    print('Lahko izbereš samo številke od 1 do 3')
else:
    barva = input('Napiši barvo robov puščice: ')
    debelost = input('Izberi debelost roba od puščice: ')
    b = input('Izberi barvo notranjosti puščice: ')
    
    x = turtle.Turtle()
    x.color(barva)
    x.pensize(debelost)
    
    if st == 1:
        prva(x, d, b)
    elif st == 2:
        druga(x, d, b)
    elif st == 3:
        tretja(x, d, b)
    
