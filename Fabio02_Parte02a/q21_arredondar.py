# 21. Realize arredondamentos de números utilizando a regra usual da matemática: 
# se a parte fracionaria for maior do que ou igual a 0,5, o numero é arredondado 
# para o inteiro imediatamente superior, caso contrario, é arredondado para o 
# inteiro imediatamente inferior.

def arredondar(n):
    inteiro = int(n // 1)
    decimais = n - inteiro

    if (decimais >= 0.5):
        return inteiro + 1
    else:
        return int(n - decimais)

def main():
    n = float(input('Insira um número decimal: '))

    print(f'{n} arrendondado -> {arredondar(n)}')


main()