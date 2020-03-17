# 9. Leia 1 (um) número entre 0 e 100, verifique e escreva se o número é ou não primo.


def eh_div(x, y):
    return x % y == 0


def eh_primo(n):
    if n <= 1:
        return False

    if eh_div(n, 2) or eh_div(n, 3) or eh_div(n, 5) or eh_div(n, 7) or eh_div(n, 9) or eh_div(n, 11):
        return False
    return True


if __name__ == '__main__':
    n = int(input('Insira um número entre 0 e 100: '))
    if n < 0 or n > 100:
        print('Número inválido')
    elif eh_primo(n):
        print(f'O número {n} é primo')
    else:
        print(f'O número {n} não é primo')
