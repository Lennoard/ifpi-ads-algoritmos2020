def main():
    n = int(input('Insira um numero: '))
    if n < 0:
        raise Exception("Deve ser positivo")

    f = n
    for i in reversed(range(1, n)):
        f = f * i

    print(f'O fatorial de {n} é {f}')


main()
