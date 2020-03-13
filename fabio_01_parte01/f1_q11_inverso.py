n = int(input('Insira um número de 3 digitos: '))
if (n > 999 or n < 100):
    raise Exception('Bruh...')

c = n // 100
d = (n % 100) // 10
u = n % 10

print(f'{n} -> {u}{d}{c}')
