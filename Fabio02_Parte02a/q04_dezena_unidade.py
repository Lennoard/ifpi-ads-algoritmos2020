# Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o
# algarismo da dezena é igual ou diferente do algarismo da unidade.


if __name__ == '__main__':
    n = int(input('Insira um número entre 10 e 100: '))

    if n < 10 or n > 100:
        print('Número inválido')
    else:
        unidade = n % 10
        dezena = n // 10

        if unidade == dezena:
            print('O algarismo da dezena é igual ao da unidade')
        else:
            print('O algarismo da dezena é diferente ao da unidade')
