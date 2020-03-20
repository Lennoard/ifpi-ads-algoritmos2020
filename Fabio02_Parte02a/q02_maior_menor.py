# Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.


if __name__ == '__main__':
    n1 = int(input('Insira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))

    if n1 > n2:
        print('O maior número é', n1)
        print('O menor número é', n2)
    else:
        print('O maior número é', n2)
        print('O menor número é', n1)
