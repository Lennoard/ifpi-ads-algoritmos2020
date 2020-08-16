def main():
    n = int(input('Insira um numero inteiro: '))
    r = range(1, n) if n >= 1 else reversed(range(n, 1))

    for i in r:
        if i % 2 == 0:
            print(i)


main()
