# Leia um número e mostre na tela se o número é positivo ou negativo.


def eh_positivo(n):
    return n >= 0


if __name__ == '__main__':
    num = int(input('Insira um número inteiro: '))

    if num == 0:
        print('O número é neutro')
    elif eh_positivo(num):
        print('O número é positivo')
    else:
        print('O número é negativo')