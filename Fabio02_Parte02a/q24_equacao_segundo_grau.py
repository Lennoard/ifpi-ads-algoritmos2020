# 24. Leia os coeficientes (A, B e C) de uma equações de 2° grau e escreva suas raízes.
# Vale lembrar que o coeficiente A deve ser diferente de 0 (zero).
from math import sqrt


def calcular_equacao_segundo_grau(a, b, c, numero_raiz=1):
    if a == 0:
        raise ValueError(f'A ({a}) deve ser != 0')

    d = delta(a, b, c)
    if d < 0:
        raise ArithmeticError(f'O delta {d} não pode ser negativo')

    if numero_raiz == 1:
        return (-b + sqrt(d)) / 2 * a
    else:
        return (-b - sqrt(d)) / 2 * a


def delta(a, b, c):
    return b**2 - (4 * a * c)


if __name__ == '__main__':
    a = float(input('Insira o coeficiente A: '))
    b = float(input('Insira o coeficiente B: '))
    c = float(input('Insira o coeficiente C: '))

    try:
        raiz1 = calcular_equacao_segundo_grau(a, b, c, 1)
        raiz2 = calcular_equacao_segundo_grau(a, b, c, 2)

        print(f'Raízes: [{raiz1}, {raiz2}]')
    except ValueError as e:
        print(f'\nErro: {e}')
    except ArithmeticError as a:
        print(f'\nErro aritmético: {a}')
