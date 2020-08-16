# Leia N , LimiteSuperior e LimiteInferior e escreva todos
# os múltiplos de N entre os limites lidos.


def main():
    n = int(input('Insira um numero: '))
    start = int(input('Insira o limite inferior: '))
    end = int(input('Insira um limite superior: '))

    r = range(start, end) if n >= 1 else reversed(range(start, end))

    print(f'Múltiplos de {n} entre {start} e {end}')
    for i in r:
        if i % n == 0:
            print(i)


main()
