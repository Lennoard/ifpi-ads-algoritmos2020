# Leia LimiteSuperior e LimiteInferior e escreva todos
# os números primos entre os limites lidos.


def main():
    start = int(input('Insira o limite inferior: '))
    end = int(input('Insira um limite superior: '))

    r = range(start, end) if start >= end else reversed(range(start, end))

    print(f'Números primos entre {start} e {end}')
    for i in r:
        if is_prime(i):
            print(i)


def is_prime(n):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break
    return prime


main()
