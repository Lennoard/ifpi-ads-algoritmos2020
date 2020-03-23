# Leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
# número. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplos:
# o 326 = 3 centenas, 2 dezenas e 6 unidades
# o 12 = 1 dezena e 2 unidades


if __name__ == '__main__':
    n = int(input('Insira um número inteiro menor que 1000: '))

    if n >= 1000:
        print('Número inválido: ')
        quit()
    else:
        centenas = n // 100
        dezenas = (n % 100) // 10
        unidades = n % 10

        if centenas > 0:
            c = 'centenas' if centenas > 1 else 'centena'
            if dezenas > 0:
                d = 'dezenas' if dezenas > 1 else 'dezena'
                if unidades > 0:
                    u = 'unidades' if unidades > 1 else 'unidade'
                    print(f'{centenas} {c}, {dezenas} {d}, {unidades} {u}')
                else:
                    print(f'{centenas} {c}, {dezenas} {d}')
            else:
                if unidades > 0:
                    u = 'unidades' if unidades > 1 else 'unidade'
                    print(f'{centenas} {c}, {unidades} {u}')
                else:
                    print(f'{centenas} {c}')
        else:
            if dezenas > 0:
                d = 'Dezenas' if dezenas > 1 else 'dezena'
                if unidades > 0:
                    u = 'unidades' if unidades > 1 else 'unidade'
                    print(f'{dezenas} {d}, {unidades} {u}')
                else:
                    print(f'{dezenas} {d}')
            else:
                if unidades > 0:
                    u = 'unidades' if unidades > 1 else 'unidade'
                    print(f'{unidades} {u}')

