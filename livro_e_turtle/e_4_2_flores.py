from e_4_0_arco import arc, turtle

def desenhar_petala(t, r, angulo):
    # angulo deve ser < 180 para ser uma pétala
    for i in range(2):
        arc(t, r, angulo)
        t.lt(180 - angulo)

def main():
    print('hey')
    n = int(input('Numero de pétalas (7): '))
    r = int(input('Tamanho das pétalas (120): '))
    angulo = int(input('Ângulo das pétalas (60): '))

    t = turtle.Turtle()
    
    for _ in range(n):
        desenhar_petala(t, r, angulo)
        t.lt(360 / n)

    turtle.mainloop()

main()