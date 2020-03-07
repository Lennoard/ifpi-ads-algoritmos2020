import turtle
from math import pi

def square(t, length):
    for _ in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, length, n):
    for _ in range(n):
        t.fd(length)
        t.lt(360 / n)

def circle(t, r):
    c = 2 * pi * r
    # length * 360 = c
    lenght = c / 360
    
    polygon(t, lenght, 360)

def arc(t, r, angle):
    c = 2 * pi * r
    #    c          360
    # _______  =  _______  ->  c*arco = angle/360
    #  angle        arco

    arco = c * (angle / 360)
    n = int(arco)
    for _ in range(n):
        t.fd(arco / n)
        t.lt(angle / n)

def main():
    bob = turtle.Turtle()
    #square(bob, 45)
    #polygon(bob, .68, 200)
    #circle(bob, 50)

    arc(bob, 80, 270)
    turtle.mainloop()

# main()