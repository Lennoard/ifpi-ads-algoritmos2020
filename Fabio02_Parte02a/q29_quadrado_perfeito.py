# Um número é um quadrado perfeito quando a raiz quadrada do número é igual à soma das dezenas
# formadas pelos seus dois primeiros e dois últimos dígitos.
# Exemplo: √9801 = 99 = 98 + 01. O número 9801 é um quadrado perfeito.
# Escreva um algoritmo que leia um número de 4 dígitos e verifique se ele é um quadrado perfeito.

if __name__ == '__main__':
    n = int(input('Insira um número entre 1000 e 9999: '))

    d1 = n // 100
    d2 = n % 100
    raiz = n ** (1 / 2)

    if d1 + d2 == raiz:
        print(f'√{n} = {raiz}, {d1} + {d2} = {raiz}')
        print(f'{n} é um quadrado perfeito')
    else:
        print(f'{n} não é um quadrado perfeito')