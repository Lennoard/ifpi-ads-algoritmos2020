# Leia 3 (três) números e escreva-os em ordem crescente.


def comparar(x, y, z=-2 ** -100) -> int:
    if x >= y and x >= z:
        return x
    if y >= x and y >= z:
        return y
    return z


if __name__ == '__main__':
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))
    n3 = int(input('Insira o terceiro número: '))

    maior = comparar(n1, n2, n3)

    if n1 == maior:
        if n2 > n3:
            print(n3)
        else:
            print(n2)
        print(comparar(n2, n3))
    elif n2 == maior:
        if n1 > n3:
            print(n3)
        else:
            print(n1)
        print(comparar(n1, n3))
    else:
        if n1 > n2:
            print(n2)
        else:
            print(n1)
        print(comparar(n1, n2))

    print(maior)
