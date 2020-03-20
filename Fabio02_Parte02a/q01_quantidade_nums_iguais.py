# Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.


if __name__ == '__main__':
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))
    n3 = int(input('Insira o terceiro número: '))

    cont = 0

    if n1 == n2:
        cont += 1
    if n2 == n1:
        cont += 1

    if n2 == n3:
        cont += 1
    if n3 == n2:
        cont += 1

    if n1 == n3:
        cont += 1
    if n3 == n1:
        cont += 1

    if n1 == n2 == n3:
        cont = 3

    print(f'Existem {cont} numero(s) iguais')

