# Desenhe um diagrama da pilha que mostre o estado do programa enquanto executa circle (bob, radius). 
# Você pode fazer a aritmética à mão ou acrescentar instruções print ao código.

from __future__ import print_function, division

import math
import turtle

def printv(vname, v):
    espacos = ' ' * (13 - len(vname))
    print('             ', f'"{vname}"{espacos}', ' ---->   ', v)

def square(t, length):
    """Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.
    """
    print('================================================================================')
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    print('================================================================================')
    print('__polyline__ ', end = ' ')
    print('"t"', '             ---->   ', t)
    printv('n', n)
    printv('length', length)
    printv('angle', angle)
    
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    print('================================================================================')
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    print('================================================================================')
    print('__arc__      ', end = ' ')
    print('"t"', '             ---->   ', t)
    printv('r', r)
    printv('angle', angle)

    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    print('================================================================================')
    print('__circle__   ', end = ' ')
    print('"r"', '             ---->   ', r)
    printv('t', t)
    arc(t, r, 360)



# the following condition checks whether we are
# running as a script, in which case run the test code,
# or being imported, in which case don't.

if __name__ == '__main__':
    print('================================================================================')
    print('============================   DIAGRAMA DA PILHA   =============================')
    print('================================================================================\n')
    print('__main__     ', end = ' ')

    bob = turtle.Turtle()
    print('"bob"', '           ---->   ', bob)
    
    # draw a circle centered on the origin
    radius = 100
    printv('radius', radius)
    
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    arc(bob, 90, 180)

    # wait for the user to close the window
    turtle.mainloop()
