# Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica: se dividirmos
# o número em dois números de dois dígitos, um composto pela dezena e pela unidade, e outro pelo
# milhar e pela centena, se somarmos estes dois novos números gerando um terceiro, o quadrado deste
# terceiro número é exatamente o número original de quatro dígitos. Por exemplo:
# 2025 -> dividindo: 20 e 25 -> somando temos 45 -> 45² = 2025.


if __name__ == '__main__':
    n = int(input('Insira um número entre 1000 e 9999: '))

    d1 = n // 100
    d2 = n % 100

    soma = d1 + d2
    quadrado = soma ** 2

    if quadrado == n:
        print(f'O número {n} atende aos requisitos pois:')
        print(f'{d1} + {d2} = {soma} -> {soma}² = {quadrado}')
    else:
        print(f'O número {n} não atende aos requisitos')

