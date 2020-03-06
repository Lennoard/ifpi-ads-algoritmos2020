import turtle
from math import pi

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

def polygon(t, n):
    for i in range(n):
        t.fd(80)
        t.lt(360 / n)

def circle(t, r):
    c = 2 * pi * r
    polygon()	

def main():
    bob = turtle.Turtle()
    #square(bob)
    circle(bob, 3.8)

    turtle.mainloop()

main()