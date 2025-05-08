import turtle

zelvak = turtle.Turtle()
d = 100

def hisa(x, d):
    """Nariše hišo"""
    kateta = (d**2 / 2) ** 0.5
    x.fd(d)
    x.lt(90)
    x.fd(d)
    x.lt(90)
    x.fd(d)
    x.lt(90)
    x.fd(d)
    x.lt(180)
    x.fd(d)
    x.rt(45)
    x.fd(kateta)
    x.rt(90)
    x.fd(kateta)
    x.rt(45)
    x.fd(d)
    x.lt(90)


hisa(zelvak, 100)