# Leia 3 (três) números, verifique e escreva o maior entre os números lidos.


def maior_numero(x, y, z=-2 ** -100) -> int:
    if x >= y and x >= z:
        return x
    if y >= x and y >= z:
        return y
    return z


if __name__ == '__main__':
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))
    n3 = int(input('Insira o terceiro número: '))

    print(f'O maior número é {maior_numero(n1, n2, n3)}')

