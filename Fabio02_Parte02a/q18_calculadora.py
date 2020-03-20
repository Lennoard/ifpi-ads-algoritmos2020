#18. Leia dois valores e uma das seguintes operações a serem executadas 
# (codificadas da seguinte forma: 1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). 
# Calcule e escreva o resultado dessa operação sobre os dois valores lidos.

def calcular(operacao, n1, n2):
    if (operacao == 1):
        return n1 + n2
    elif operacao == 2:
        return n1 - n2
    elif operacao == 3:
        return n1 * n2
    elif operacao == 4:
        return n1 / n2
    else:
        raise ValueError(f'Valor inválido para "operacao", esparado 1..4 mas obteve {operacao}')


def main():
    print('|===  CALCULADORA  ===|')
    print('|                     |')
    print('| 1 - Adição          |')
    print('| 2 - Subtração       |')
    print('| 3 - Multiplicação   |')
    print('| 4 - Divisão         |')
    print('|                     |')
    print('|===  CALCULADORA  ===|\n')

    operacao = int(input('Escolha uma operação (1/2/3/4): '))

    n1 = int(input('\nInsira o primeiro número: '))
    n2 = int(input('Insira o segundo número: '))

    try:
        resultado = calcular(operacao, n1, n2)

        print(f'\nResultado: {resultado}')
    except Exception as e:
        print(str(e))


main()