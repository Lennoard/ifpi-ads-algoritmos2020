import turtle

def triangulo(t, lado):
    for _ in range(3):
        t.fd(lado)
        t.lt(120)

def pizza(t, lado, pedacos):
    for _ in range(pedacos):
        triangulo(t, int(lado / pedacos))
        t.lt(lado / pedacos)

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length * n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2 * angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length * n)

def main():
    t = turtle.Turtle()
    draw(t, 10, 10)

    turtle.mainloop()

main()