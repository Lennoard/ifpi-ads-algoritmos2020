# Leia o preço de três produtos e informe qual produto deve ser comprado, sabendo que a decisão é
# sempre pelo mais barato.


def menor(p1, p2, p3):
    m = p1

    if p2 < p1:
        m = p2

    if preco3 < m:
        m = p3

    return m


if __name__ == '__main__':
    preco1 = float(input('Insira o preço do produto 01: '))
    preco2 = float(input('Insira o preço do produto 02: '))
    preco3 = float(input('Insira o preço do produto 03: '))

    menor_preco = menor(preco1, preco2, preco1)

    if menor_preco == preco1:
        print('Produto 1 deverá ser comprado pois é o mais barato')
    elif menor_preco == preco2:
        print('Produto 2 deverá ser comprado pois é o mais barato')
    else:
        print('Produto 3 deverá ser comprado pois é o mais barato')


